from rest_framework import serializers
from .models import Blog, CustomUser, Comment, Like

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','email','password','password2']
        read_only_fields = ['id']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password or password2:
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password":"Both passwords don't match."})
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        



class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    class Meta:
        model = Like
        fields = ['user','blog','posted_at']
        read_only_fields = ['user','blog','posted_at'] 

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['author','blog','content','posted_at']
        read_only_fields = ['author','blog','posted_at']

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    image_url = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Blog
        fields = ['title','subtitle','slug','content','published_at','like_count','author','image_url','comments']

    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.img and request:
            return request.build_absolute_uri(obj.img.url)
        return None
    
    def get_like_count(self, obj):
        blog = Blog.objects.get(title=obj.title)
        likes = blog.likes.all()
        likes = likes.count()
        return likes
        

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ['author','blog','content','posted_at']
        read_only_fields = ['author','blog','posted_at']


