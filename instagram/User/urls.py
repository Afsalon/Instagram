from django.urls import path,include
from User.views import UserAPI,UserDataAPI,CurrentUserAPI,UserPutAPI,UserListAPI,ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('signup/', UserAPI.as_view(), name = "user_view"),
    path('<str:username>/', UserDataAPI.as_view(),name="profile_page"),
    path('current/user/',CurrentUserAPI.as_view(), name="current_user"),
    path('edit/user/',UserPutAPI.as_view(), name="Edit_user"),
    path('user/list/<str:username>/',UserListAPI.as_view(), name="user_list"),
    path('change/password/view/',ChangePasswordView.as_view(), name="change_password_page")
]
