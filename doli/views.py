from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from doli import permissions
from .serializers import *
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Post,Like,Comment
from rest_framework.viewsets import ModelViewSet

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [AllowAny]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthorAuthentiocation]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthorAuthentiocation]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthorAuthentiocation]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        