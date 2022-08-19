from rest_framework.response import Response
from rest_framework.views import APIView
from Follow.serializers import FollowSerializer,FollowPostSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from Follow.models import Follow

User = get_user_model()
class FollowAPI(APIView):
    serializer_class = FollowPostSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request,format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UnFollowAPI(APIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    def delete(self,request,pk,format = None):
        try:
            following_obj = User.objects.get(pk = pk)
            follow_obj = Follow.objects.get(user=request.user,following=following_obj)
            follow_obj.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        except:
            return Response({"status":"invalid"})

class FollowingAPI(APIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request,username,count,format = None):
        j = 10 * count
        i = j - 10
        try:
            user = User.objects.get(username=username)
        except:
            return Response({},status=status.HTTP_204_NO_CONTENT)
        try:
            follow_list = Follow.objects.filter(user = user)
        except:
            follow_list = []
        serializer = self.serializer_class(follow_list,many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

class FollowedAPI(APIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request,username,count,format = None):
        j = 10 * count
        i = j - 10
        try:
            user = User.objects.get(username=username)
        except:
            return Response({},status=status.HTTP_204_NO_CONTENT)
        try:
            follow_list = Follow.objects.filter(following = user)
        except:
            follow_list = []
        serializer = self.serializer_class(follow_list,many=True)
        serialized_data = serializer.data
        return Response(serialized_data)
class IsFollowAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,username,format = None):
        try:
            user = User.objects.get(username=request.user.username)
            other_user = User.objects.get(username = username)
        except:
            return Response({},status=status.HTTP_204_NO_CONTENT)
        try:
            follow_list = Follow.objects.get(user=user, following = other_user)
            return Response({"state":True,"follow":True})
        except:
            if other_user.is_public:
                return Response({"state":True,"follow":False})
            return Response({"state":False,"follow":False})
