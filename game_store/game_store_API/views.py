from rest_framework import status,generics, viewsets
from rest_framework.response import Response
from .serializers import CategorySerializer, ComponentSerializer, ComponentTypeSerializer, ManufacturerSerializer, RegisterSerializer, TokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenViewBase
from .models import Component, ComponentType, Manufacturer, User, ProductCategory
from .permissions import AdminUserOrReadOnly, UserIsAdmin
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

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


class ApproveViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=False).order_by('id')
    permission_classes = [UserIsAdmin,]
    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True,context={'request': request})
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the users",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested user data",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    
    def update(self, request, pk = None, *args, **kwargs):
        user = get_object_or_404(self.queryset,pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        data = request.data
        try:
            user.is_active = data["is_active"]
            user.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "User successfully approved.",
                "data": serializer.data
            },status = status.HTTP_201_CREATED)
        except:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "User not approved.",
            },status = status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None, *args, **kwargs):
        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        return Response({
            "status": status.HTTP_202_ACCEPTED,
            "success": True,
            "message": "User successfully deleted."
        },status = status.HTTP_202_ACCEPTED)


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.all().order_by('id')
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AdminUserOrReadOnly]
    model = ProductCategory
    def get_queryset(self):
        return self.model.objects.all()
    def list(self, request, *args, **kwargs):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the categories",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    def retrieve(self, request, pk=None, *args, **kwargs):
        category = get_object_or_404(self.queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested category data",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    def perform_create(self, serializer):
        serializer.save()


class ManufacturerView(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all().order_by('id')
    permission_classes = [AdminUserOrReadOnly]
    model = Manufacturer
    def get_queryset(self):
        return self.model.objects.all()
    def list(self, request, *args, **kwargs):
        serializer = ManufacturerSerializer(self.queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the manufacturers",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    def retrieve(self, request, pk=None, *args, **kwargs):
        manufacturer = get_object_or_404(self.queryset, pk=pk)
        serializer = ManufacturerSerializer(manufacturer)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested manufacturer data",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "Manufacturer Created Successfully.",
                "data": serializer.data,
            },status = status.HTTP_201_CREATED)
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "Manufacturer not created"
            },status = status.HTTP_400_BAD_REQUEST)


class ComponentTypeView(viewsets.ModelViewSet):
    serializer_class = ComponentTypeSerializer
    queryset = ComponentType.objects.all().order_by('id')
    permission_classes = [AdminUserOrReadOnly]
    model = ComponentType
    def get_queryset(self):
        return self.model.objects.all()
    def list(self, request, *args, **kwargs):
        serializer = ComponentTypeSerializer(self.queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the component types",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    def retrieve(self, request, pk=None, *args, **kwargs):
        type = get_object_or_404(self.queryset, pk=pk)
        serializer = ComponentTypeSerializer(type)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested component type data",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "Component type Created Successfully.",
                "data": serializer.data,
            },status = status.HTTP_201_CREATED)
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "Component type not created"
            },status = status.HTTP_400_BAD_REQUEST)


class ComponentView(viewsets.ModelViewSet):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all().order_by('id')
    # permission_classes = [AdminUserOrReadOnly]
    model = Component
    def get_queryset(self):
        return self.model.objects.all()
    def list(self, request, *args, **kwargs):
        serializer = ComponentSerializer(self.queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the components",
                "data": serializer.data
            },status = status.HTTP_200_OK)