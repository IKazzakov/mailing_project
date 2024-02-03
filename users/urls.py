from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserListView, set_user_status, \
    ProfileUpdateView, VerifyEmail, CustomLoginView, CustomPasswordResetView, CustomPasswordResetDoneView, \
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, SuccessVerifyView, ErrorVerifyView

app_name = UsersConfig.name


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/<token>/', VerifyEmail.as_view(), name='verify_email'),
    path('success_verify/', SuccessVerifyView.as_view(), name='success_verify'),
    path('error_verify/', ErrorVerifyView.as_view(), name='error_verify'),

    path('profile/', ProfileUpdateView.as_view(), name='profile'),

    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('users_list/', login_required(UserListView.as_view()), name='users_list'),
    path('users_status/<int:pk>/', set_user_status, name='users_status'),

]