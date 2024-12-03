from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        # Custom delete method to handle specific scenarios
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)  # No content status for successful deletion