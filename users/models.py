from django.contrib.auth.models import User
from django.db import models


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.BigIntegerField(default=0000000000)

    def __str__(self):
        return str(self.user.username)
