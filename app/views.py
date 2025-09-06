from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer, CustomUserSerializer
from .models import Blog, Comment, Like, CustomUser
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class CustomUserWriteSelfOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT','PATCH','DELETE']:
            user_id = request.user.id
            pk = view.kwargs.get('pk')
            if pk is not None and user_id == int(pk):
                return True
            return False
        return True
        
class CustomUserViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated,CustomUserWriteSelfOnly]
    authentication_classes = [TokenAuthentication]

class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [IsAuthenticated]

