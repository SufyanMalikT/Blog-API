from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer, CustomUserSerializer
from .models import Blog, Comment, Like, CustomUser
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
# Create your views here.

class CustomUserPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT','PATCH','DELETE']:
            user_id = request.user.id
            pk = view.kwargs.get('pk')
            if pk is not None and user_id == int(pk):
                return True
            return False
        return True

class BlogPermissionsClass(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if view.action in ['like','comment']:
            return True

        return obj.author == request.user
        
class CustomUserViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated,CustomUserPermissions]


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [AllowAny()]
        return [IsAuthenticated(),BlogPermissionsClass()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True,methods=['POST'])
    def like(self, request, pk=None):
        blog = self.get_object()
        if request.user.is_authenticated:
            try:
                like = Like.objects.create(user=request.user,blog=blog)
                like.save()
                return Response({"Success":f"You've liked {blog.author.username}'s post"},status=200)
            except IntegrityError:
                return Response({"Failed":"You've already liked this post"},status=400)
        return Response({"Failed":"Please provide the necessary credentials in order to like or comment on posts."},status=403)
    
    @action(detail=True,methods=['POST'])
    def comment(self, request, pk=None):
        blog = self.get_object()
        if request.user.is_authenticated:
            data = {
                'blog':blog.title,
                'author':request.user.username,
                'content':request.data.get('content')
            }
            serializer = CommentSerializer(data=data,context={'request':request,'blog':blog})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors)
        return Response({'Failed':'Please provide the required credentials.'})



