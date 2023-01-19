"""
Definition of models.
"""
from django.utils.translation import gettext_lazy as _

from django.db import models

def upload_to(instance, filename):
    return f'asset_img/{filename}'

# Create your models here.
class Animal(models.Model):
    choice = (('YES','yes'), ('NO','no'))
    ani_class = (('Young', 'Young'), ('Adult', 'Adult'), ('Senior', 'Senior'))
    ani_size = (('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'))
    ani_activity_level = (('Small', 'Small'), ('Medium', 'Medium'), ('High', 'High'))
    animal_name = models.CharField(max_length=20, null=True)
    animal_age = models.IntegerField(default=34, null=True)
    animal_class = models.CharField(max_length=10, choices=ani_class, default='small')
    animal_type = models.CharField(max_length=10, null=True)
    likes_cats = models.CharField(max_length=3, default='no', choices=choice)
    likes_kids = models.CharField(max_length=3, default='no', choices=choice)
    likes_dogs = models.CharField(max_length=3, default='no', choices=choice)
    size = models.CharField(max_length=10, choices=ani_size, default='small')
    activity_level = models.CharField(max_length=10, choices=ani_activity_level, default='small')
    bio = models.TextField(max_length=2000, null=True)
    photo = models.ImageField(_('Image'), null=True, upload_to=upload_to, default='asset_img/default.jpg')
    
    class Meta:
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name