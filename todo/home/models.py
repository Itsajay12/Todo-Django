from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profilepicture=models.ImageField(upload_to='profi')
    def __str__(self) :
        return f"{self.user}"
class TodoList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField( max_length=50)
    enddate=models.DateField( auto_now=False)
    adddate=models.DateField( auto_now=True)
    status=models.CharField( max_length=50,default="pending")
    is_imp=models.BooleanField(default=False)
    def __str__(self) :
        return f"{self.user}"