from django.contrib.auth.models import User
from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


    @property
    def count_reviews(self):
        return self.reviews.all().count()

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(women=self)
        return [{'id': i.id, 'text': i.text} for i in reviews]


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    women = models.ForeignKey(Women, on_delete=models.CASCADE, null=True, related_name='reviews')


    def __str__(self):
        return self.text
