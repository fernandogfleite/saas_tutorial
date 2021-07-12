from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from core.views import CompanySafeViewMixin
from . import serializers

User = get_user_model()

class AccountCreate(generics.CreateAPIView):
    name = 'account-create'
    serializer_class = serializers.AccountSerializer


class UserList(CompanySafeViewMixin,generics.ListCreateAPIView):
    name = 'user-list'
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class UserDetail(CompanySafeViewMixin,generics.RetrieveUpdateDestroyAPIView):
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class CompanyDetail(generics.RetrieveDestroyAPIView):
    name = 'company-detail'
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = serializers.CompanySerializer

    def get_object(self):
        return self.request.user.company
