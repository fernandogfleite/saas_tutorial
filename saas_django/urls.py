from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/user-messages/', include('user_messages.urls')),
    path('api/v1/auth/', include('rest_framework.urls'))
]
