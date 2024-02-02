from django.conf import settings
from django.core.cache import cache


def cache_message(model, key):
    queryset = model.objects.all()
    if settings.CACHE_ENABLED:
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)
        return cache_data
    return queryset
