from rest_framework import status,generics, permissions, viewsets, views
from rest_framework.response import Response
from .serializers import RegisterSerializer, TokenObtainPairSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenViewBase
from .models import User


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "message": "User Created Successfully.",
                "data": UserSerializer(user, context=self.get_serializer_context()).data,
            })
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "massage": "User with the same username or email already exists."
            })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetails(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer