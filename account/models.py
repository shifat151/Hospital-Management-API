import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(_('first name'), max_length=150)
    status=models.BooleanField(default=False)
    
