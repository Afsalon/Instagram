from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from User.serializers import UserSerializer,UserGetSerializer,UserPutSerializer,ChangePasswordSerializer
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

User = get_user_model()


class UserAPI(APIView):
    serializer_class = UserSerializer
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserDataAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=UserGetSerializer
    def get(self, request, username, format = None):
        try:
            user_obj = User.objects.get(username = username)
            serializer = self.serializer_class(user_obj)
            serialized_data = serializer.data
            return Response(serialized_data)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)

class CurrentUserAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=UserGetSerializer
    def get(self, request,format= None):
        try:
            user_obj = User.objects.get(username = request.user.username)
            serializer = self.serializer_class(user_obj)
            serialized_data = serializer.data
            return Response(serialized_data)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
class UserPutAPI(APIView):
    serializer_class = UserPutSerializer
    permission_classes = [IsAuthenticated]
    def put(self, request, format = None):
        try:
            user_obj = User.objects.get(pk=request.user.pk)
        except:
            return Response({'Error':'No such user'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(user_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserListAPI(APIView):
    serializer_class = UserGetSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, username, format = None):
        try:
            user_list = User.objects.filter(Q(username__startswith=username)|Q(full_name__startswith=username))
            serializer = self.serializer_class(user_list,many=True)
            serialized_data = serializer.data
            return Response(serialized_data)
        except:
            return Response([],status = status.HTTP_204_NO_CONTENT)

class ChangePasswordView(generics.UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = [IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
