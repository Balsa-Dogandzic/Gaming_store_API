"""URLs for the API"""
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from .views import (ApproveViewSet,CategoryView,ComponentTypeView,ComponentView,ManufacturerView,
ProductView, ProfileView,RatingsView,RegisterView,SpecificationView,TokenObtainPairView)

router = DefaultRouter()
router.register(r'inactive', ApproveViewSet, basename='user')
router.register(r'category', CategoryView, basename='category')
router.register(r'manufacturer', ManufacturerView, basename='manufacturer')
router.register(r'component_type', ComponentTypeView, basename='component_type')
router.register(r'component', ComponentView, basename='component')
router.register(r'product', ProductView, basename='product')
router.register(r'specifications', SpecificationView, basename='specifications')
router.register(r'rating', RatingsView, basename='rating')
router.register(r'profile', ProfileView, basename='profile')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('', include(router.urls)),
]
