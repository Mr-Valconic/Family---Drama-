from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),


    # Accounts (Login, Register, Dashboard, Add Member)
    path('accounts/', include('accounts.urls')),


    # Home
    path('', include('home.urls')),

]


# Media files (uploaded images)

if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT

    )