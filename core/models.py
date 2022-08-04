from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio: models.TextField(blank=True)
    # Where will image upload to when user uploads the image
    avatar: models.ImageField(upload_to='profile_images', default='blank-profile-picture-g40283e0de_1280')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
