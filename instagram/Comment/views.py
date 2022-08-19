from Comment.serializers import CommentSerializer,CommentPostSerializer
from Comment.models import Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from Post.models import Post
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
class CommentAPI(APIView):
    serializer_class = CommentPostSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RemoveCommentAPI(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,pk,format = None):
        comments = Comment.objects.filter(post=pk)
        serializer = self.serializer_class(comments, many = True)
        serialized_data = serializer.data
        return Response(serialized_data)

    def delete(self,request,pk,format = None):
        try:
            comment_obj = Comment.objects.get(pk=pk)
            comment_obj.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except:
            return Response({"status":"invalid"})
