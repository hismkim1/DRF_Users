from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from .serializers import UserSerializer


class UserListAPI(APIView):
    def get(self, request):
        queryset = User.objects.all()
        print(queryset)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

