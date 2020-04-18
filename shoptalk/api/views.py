from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics, permissions
from .serializers import ItemSerializer, MallSerializer, CategorySerializer
from .models import Item, Mall, Category


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ItemSerializer

    def get_queryset(self):
        return self.request.user.items.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MallViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mall.objects.all()
    serializer_class = MallSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GetItemsList(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['mallId']
        return Item.objects.filter(mallId=username)
