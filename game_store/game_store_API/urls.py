from django.urls import path
from .views import RegisterView, UserDetails, UserViewSet, TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('users/',UserViewSet.as_view({'get':'list'})),
    path('users/<int:pk>/', UserDetails.as_view()),
]