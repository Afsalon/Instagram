from rest_framework.response import Response
from rest_framework.views import APIView
from Like.serializers import LikeSerializer
from Post.models import Post
from rest_framework import status
from django.contrib.auth import get_user_model
from Like.models import Like
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
class LikeAPI(APIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RemoveLikeAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,pk,format= None):
        try:
            post_obj = Post.objects.get(pk = pk)
            like_obj = Like.objects.get(user=request.user, post=post_obj)
            return Response({"state":True})
        except:
            return Response({"state":False})
    def delete(self,request,pk,format = None):
        try:
            post_obj = Post.objects.get(pk=pk)
            like_obj = Like.objects.get(post=post_obj,user=request.user)
            like_obj.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except:
            return Response({"status":"invalid"})
