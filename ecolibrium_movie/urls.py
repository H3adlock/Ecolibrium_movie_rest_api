from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from movies import urls as movie_url
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-token-auth/', obtain_auth_token),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api', include(movie_url))
              ]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
