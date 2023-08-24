from django.db import models
from user.models import User


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'categories'
    
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='recipes',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    thumbnail = models.URLField( null=True, blank=True)
    image =models.FileField( upload_to='image/', max_length=100)
    ingredients = models.JSONField()
    instructions = models.TextField()
    measures = models.JSONField()
    source = models.URLField()
    youtube = models.URLField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='reviews',
                               on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.recipe} comment'


class Upvote(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='upvotes',
                               on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'voted_by')
        
        
        
class Profile(models.Model):
    organization_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Profile/')
    contact = models.CharField(max_length=100, null=True, default=None)
    website = models.CharField(max_length=100, null = True, default=None)
    address = models.CharField(max_length=150, null =True, default=None)
    location = models.CharField(max_length = 150, null= True ,default=None)
    Gender = models.CharField(max_length=160, null=True, default=None)
    
    def __str__(self):
        return f'{self.name}'


class ImageModel(models.Model):
    organization_id = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')      