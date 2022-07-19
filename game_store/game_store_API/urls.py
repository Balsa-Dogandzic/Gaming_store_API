from django.urls import path
from .views import RegisterView, UserDetails, InactiveUsersSet, TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('inactive/',InactiveUsersSet.as_view()),
    path('users/<int:pk>/', UserDetails.as_view()),
]