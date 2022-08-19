from rest_framework.response import Response
from rest_framework.views import APIView
from Post.serializers import PostSerializer
from Post.models import Post
from Follow.models import Follow
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


User = get_user_model()
class PostAPI(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request,count,format = None):
        j = 10*count
        i = j - 10
        user = request.user
        following = user.current_user.all()
        lst = [i.following for i in following]
        following_posts = Post.objects.filter(Q(user__in=lst,user__is_public=False)|Q(user__is_public=True)|Q(user=request.user)).order_by('-created_date')[i:j]
        serializer = self.serializer_class(following_posts,many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

class PostPostAPI(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPI(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format = None):
        post_obj = Post.objects.get(pk = pk)
        user_obj = User.objects.get(pk = post_obj.user.pk)
        is_me = user_obj.username == request.user.username
        try:
            follow_obj = Follow.objects.get(user=request.user, following = user_obj)
            is_follow = True
        except:
            is_follow = False
        try:
            if is_follow or user_obj.is_public or is_me:
                post_obj = Post.objects.get(pk = pk)
                serializer = self.serializer_class(post_obj)
                serialized_data = serializer.data
                return Response(serialized_data)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format = None):
        try:
            post_obj = Post.objects.get(pk = pk)
            post_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"Object":"DoesNotExist"})

class ProfilePostAPI(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, username, format = None):
        try:
            user = User.objects.get(username=request.user.username)
            other_user = User.objects.get(username = username)
        except:
            return Response({},status=status.HTTP_204_NO_CONTENT)
        try:
            follow_obj = Follow.objects.get(user=user,following = other_user)
            is_follow = True
        except:
            is_follow = False

        if (user and username == request.user.username) or is_follow or other_user.is_public:
            posts = Post.objects.filter(user=other_user)
            serializer = self.serializer_class(posts, many = True)
            serialized_data = serializer.data
            return Response(serialized_data)
        else:
            return Response([])
