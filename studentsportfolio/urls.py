from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include('main.urls')),
    path('auth/', obtain_auth_token)
]
