"""Create your views here"""
from django.shortcuts import get_object_or_404
from rest_framework import status, generics,viewsets,response,parsers,permissions
from rest_framework_simplejwt.views import TokenViewBase
from .serializers import (CategorySerializer,ComponentSerializer,ComponentTypeSerializer,
DetailedComponentSerializers,ManufacturerSerializer,ProductListSerializer,ProductRetrieveSerializer,
ProductSerializer, RatingSerializer,RegisterSerializer,SpecificationDetailSerializer,
SpecificationSerializer,TokenObtainPairSerializer,UserSerializer)
from .models import (Component,ComponentType,Manufacturer,Product, Rating,
Specifications,User,ProductCategory)
from .permissions import AdminUserOrReadOnly, UserIsAdmin
# pylint: disable=too-many-ancestors
# pylint: disable=no-member


class RegisterView(generics.GenericAPIView):
    """Class for user registration"""
    serializer_class = RegisterSerializer
    def post(self, request):
        """POST request for user registration"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "User Created Successfully.",
            "data": UserSerializer(user, context=self.get_serializer_context()).data,
        },status = status.HTTP_201_CREATED)


class ApproveViewSet(viewsets.ModelViewSet):
    """Class for inactive user approvement"""
    serializer_class = UserSerializer
    permission_classes = [UserIsAdmin,]

    def get_queryset(self):
        queryset = User.objects.filter(is_active=False).order_by('id')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True,context={'request': request})
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all inactive users",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None,**kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested user data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def update(self, request, *args, pk = None,**kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset,pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        data = request.data
        try:
            user.is_active = data["is_active"]
            user.save()
            return response.Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "User successfully approved.",
                "data": serializer.data
            },status = status.HTTP_201_CREATED)
        except KeyError:
            return response.Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "User not approved.",
            },status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,*args,pk=None,**kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return response.Response({
            "status": status.HTTP_202_ACCEPTED,
            "success": True,
            "message": "User successfully deleted."
        },status = status.HTTP_202_ACCEPTED)


class TokenObtainPairView(TokenViewBase):
    """Class for user login"""
    serializer_class = TokenObtainPairSerializer


class CategoryView(viewsets.ModelViewSet):
    """Category view class"""
    serializer_class = CategorySerializer
    parser_classes = (parsers.MultiPartParser,parsers.FormParser)
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return ProductCategory.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the categories",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.get_queryset()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return response.Response({
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
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Category Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)


class ManufacturerView(viewsets.ModelViewSet):
    """Manufacturer view class"""
    serializer_class = ManufacturerSerializer
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return Manufacturer.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ManufacturerSerializer(queryset, many=True)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the manufacturers",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.get_queryset()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializer(manufacturer)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested manufacturer data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Manufacturer Created Successfully.",
            "data": serializer.data
        },status = status.HTTP_201_CREATED)


class ComponentTypeView(viewsets.ModelViewSet):
    """Component type view class"""
    serializer_class = ComponentTypeSerializer
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return ComponentType.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ComponentTypeSerializer(queryset, many=True)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the component types",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.get_queryset()
        category_type = get_object_or_404(queryset, pk=pk)
        serializer = ComponentTypeSerializer(category_type)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested component type data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Component type Created Successfully.",
            "data": serializer.data
        },status = status.HTTP_201_CREATED)


class ComponentView(viewsets.ModelViewSet):
    """Component view class"""
    serializer_class = ComponentSerializer
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return Component.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DetailedComponentSerializers(queryset, many=True)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the components",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.get_queryset()
        component = get_object_or_404(queryset, pk=pk)
        serializer = DetailedComponentSerializers(component)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested component data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Component type Created Successfully.",
            "data": serializer.data
        },status = status.HTTP_201_CREATED)


class ProductView(viewsets.ModelViewSet):
    """Product view class"""
    serializer_class = ProductSerializer
    permission_classes = [AdminUserOrReadOnly]
    parser_classes = (parsers.MultiPartParser,parsers.FormParser)

    def get_queryset(self):
        queryset = Product.objects.all().order_by('id')
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__name = category)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductListSerializer(queryset, many=True, context={'request': request})
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the products",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.get_queryset()
        component = get_object_or_404(queryset, pk=pk)
        serializer = ProductRetrieveSerializer(component,context={'request': request})
        return response.Response({
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
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Product Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)


class SpecificationView(viewsets.ModelViewSet):
    """Spec view class"""
    serializer_class = SpecificationSerializer
    permission_classes = [AdminUserOrReadOnly]

    def get_queryset(self):
        return Specifications.objects.all().order_by('average_rating')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SpecificationSerializer(queryset, many=True)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the specs",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        queryset = self.get_queryset()
        specification = get_object_or_404(queryset, pk=pk)
        serializer = SpecificationDetailSerializer(specification)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Requested spec data",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Specification Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)

class RatingsView(viewsets.ModelViewSet):
    """Ratings view class"""
    serializer_class = RatingSerializer
    # permission_classes = [permissions.IsAuthenticated,]
    def get_queryset(self):
        queryset = Rating.objects.all().order_by('id')
        product_name = self.request.query_params.get('product')
        if product_name is not None:
            queryset = queryset.filter(product__name = product_name)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RatingSerializer(queryset,many=True)
        return response.Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "List of all the ratings",
                "data": serializer.data
            },status = status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None,**kwargs):
        queryset = self.get_queryset()
        rating = get_object_or_404(queryset, pk=pk)
        serializer = RatingSerializer(rating)
        return response.Response({
            "status":status.HTTP_200_OK,
            "success":True,
            "message":"Requested rating retrieved",
            "data":serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return response.Response({
            "status": status.HTTP_201_CREATED,
            "success": True,
            "message": "Rating Created Successfully.",
            "data": serializer.data,
        },status = status.HTTP_201_CREATED)
