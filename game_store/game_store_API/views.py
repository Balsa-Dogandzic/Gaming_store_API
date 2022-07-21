from rest_framework import status,generics, views
from rest_framework.response import Response
from .serializers import RegisterSerializer, TokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenViewBase
from .models import User
from .permissions import UserIsAdmin


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "User Created Successfully.",
                "data": UserSerializer(user, context=self.get_serializer_context()).data,
            },status = status.HTTP_201_CREATED)
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                'success': False,
                "message": "User with the same username or email already exists."
            },status = status.HTTP_400_BAD_REQUEST)


class InactiveUsersSet(views.APIView):
    permission_classes = [UserIsAdmin,]

    serializer_class = UserSerializer
    def get(self, request, format=None):
        inactive_users = User.objects.filter(is_active=False).order_by('id')
        serializer = UserSerializer(inactive_users,many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "List of all inactive users",
            "data": serializer.data
        },status = status.HTTP_200_OK)


class UserDetails(views.APIView):
    permission_classes = [UserIsAdmin,]

    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "success": False,
                "message": "User not found."
            },status = status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "Requested user data",
            "data":serializer.data
            },status= status.HTTP_200_OK)
    def put(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        data=request.data
        try:
            user.is_active = data["is_active"]
            user.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                'success': True,
                'message': 'User approved succesfully'
            },status = status.HTTP_201_CREATED)
        except:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                'success': False,
                'message': 'User not approved'
                },status = status.HTTP_400_BAD_REQUEST)


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer