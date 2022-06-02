from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404


from .models import Cat
from .serializers import CatListSerializer, CatDetailSerializer


# ========================================= GENERIC VIEWS =========================================================#


class CatListCreateAPIView(
    # StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatListSerializer
    # authentication_classes = [                     # we don't need them, have them in settings
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    #     # authentication.TokenAuthentication        # this has been redefined
    # ]   #
    # permission_classes = [permissions.IsAuthenticated]           # add permissions
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class ProductDetailAPIView(
    # StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


class ProductUpdateAPIView(
    # StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(
    # StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)
