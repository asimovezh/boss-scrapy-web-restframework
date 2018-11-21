from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .models import  Boss
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BossViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Boss to be viewed or edited.
    """
    queryset = Boss.objects.all()
    serializer_class = GroupSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    只允许作者修改但允许所有人读的权限设置
    """
    def has_object_permission(self, request, view, obj):
        # 所有用户都允许读取,所以安全的http方法会直接放行
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True
        # 写入权限需要作者本人
        return obj.author == request.user