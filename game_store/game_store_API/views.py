from logging import raiseExceptions
from rest_framework import status,generics, viewsets
from rest_framework.response import Response
from .serializers import CategorySerializer, ComponentSerializer, ComponentTypeSerializer, DetailedComponentSerializers, ManufacturerSerializer, ProductListSerializer, ProductRetrieveSerializer, ProductSerializer, RegisterSerializer, SpecificationDetailSerializer, SpecificationSerializer, TokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenViewBase
from .models import Component, ComponentType, Manufacturer, Product, Specifications, User, ProductCategory
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
    permission_classes = [UserIsAdmin,]

    def get_queryset(self):
        queryset = User.objects.filter(is_active=False).order_by('id')
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True,context={'request': request})
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all inactive users",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested user data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def update(self, request, pk = None, *args, **kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset,pk=pk)
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
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
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
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return ProductCategory.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the categories",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested category data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Category Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)


class ManufacturerView(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return Manufacturer.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ManufacturerSerializer(queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the manufacturers",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializer(manufacturer)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested manufacturer data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Manufacturer Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)
        


class ComponentTypeView(viewsets.ModelViewSet):
    serializer_class = ComponentTypeSerializer
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return ComponentType.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ComponentTypeSerializer(queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the component types",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        type = get_object_or_404(queryset, pk=pk)
        serializer = ComponentTypeSerializer(type)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested component type data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Component type Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)
        


class ComponentView(viewsets.ModelViewSet):
    serializer_class = ComponentSerializer
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return Component.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DetailedComponentSerializers(queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the components",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        component = get_object_or_404(queryset, pk=pk)
        serializer = DetailedComponentSerializers(component)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested component data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Component type Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [AdminUserOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = Product.objects.all().order_by('id')  
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__name = category)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductListSerializer(queryset, many=True, context={'request': request})
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the products",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        component = get_object_or_404(queryset, pk=pk)
        serializer = ProductRetrieveSerializer(component,context={'request': request})
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested product data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Product Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)


class SpecificationView(viewsets.ModelViewSet):
    serializer_class = SpecificationSerializer
    permission_classes = [AdminUserOrReadOnly]
    model = Specifications

    def get_queryset(self):
        return Specifications.objects.all().order_by('id')    

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SpecificationSerializer(queryset, many=True)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the specs",
                "data": serializer.data
            },status = status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        specification = get_object_or_404(queryset, pk=pk)
        serializer = SpecificationDetailSerializer(specification)
        return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested spec data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Specification Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)
