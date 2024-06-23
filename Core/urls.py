from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('profile/<int:id>/', profile, name='profile'),
    path('', include('kinopoisk.urls')),
    path('api-auth/', include('rest_framework.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

