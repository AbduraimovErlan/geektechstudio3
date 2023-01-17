from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from women.models import Review
from women.serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']



class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


class RegisterAPIView(APIView):
    serializer_class = UserCreateSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'User created'},
                        status=status.HTTP_201_CREATED)



