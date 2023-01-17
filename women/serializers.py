from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from women.models import Women, Review


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ("id", "title", "image", "description", "cat")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



