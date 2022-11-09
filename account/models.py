from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=30)
    natinal_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profile/image", blank=True, null=True)


    def __str__(self) -> str:
        return self.user.username