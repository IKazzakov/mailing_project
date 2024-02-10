import secrets

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

# Create your views here.


from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView, LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, TemplateView

from users.forms import CustomUserChangeForm, CustomUserRegisterForm, \
    CustomAuthenticationForm, CustomPasswordResetForm, CustomResetConfirmForm
from users.models import User


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.set_is_active'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = User
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        token = secrets.token_urlsafe(32)
        new_user.verification_code = token
        new_user.save()
        activation_url = reverse_lazy('users:verify_email', kwargs={'token': token})
        send_mail(
            subject='Активация аккаунта на нашей платформе',
            message=f'Ссылка для активации учетной записи: http://127.0.0.1:8000{activation_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class VerifyEmail(View):
    def get(self, request, token):
        try:
            user = User.objects.get(verification_code=token)
            user.is_active = True
            user.save()
            return redirect('users:success_verify')
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return redirect('users:error_verify')


class SuccessVerifyView(TemplateView):
    template_name = 'users/success_verify.html'


class ErrorVerifyView(TemplateView):
    template_name = 'users/error_verify.html'


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:login')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')
    email_template_name = 'users/email_reset.html'
    from_email = settings.EMAIL_HOST_USER


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomResetConfirmForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


@permission_required(perm='users.set_is_active')
def set_user_status(request, pk):
    obj = get_object_or_404(User, pk=pk)
    if obj.is_superuser:
        return HttpResponseForbidden()
    if obj.is_active:
        obj.is_active = False
    else:
        obj.is_active = True
    obj.save()

    return redirect(request.META.get('HTTP_REFERER'))
