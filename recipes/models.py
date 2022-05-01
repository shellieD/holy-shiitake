"""MODELS"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Added"))


class Recipe(models.Model):
    """Recipe Model"""
    recipe_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipes"
    )
    added_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    recipe_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name="recipe_likes",
        blank=True
    )


class Meta:
    ordering = ['-added_on']

    def __str__(self):
        return self.recipe_name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Comments Model"""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(max_length=50, unique=True)
    added_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    likes = models.ManyToManyField(
        User,
        related_name="comment_likes",
        blank=True
    )
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['added_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"