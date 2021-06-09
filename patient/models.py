from django.db import models
from account.models import User

# Create your models here.

class patient(models.Model):
    age= models.PositiveIntegerField()
    address= models.TextField()
    mobile=models.CharField(max_length=20)
    status=models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.username

    