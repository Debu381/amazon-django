from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ User Profile Category Model Class 
        Django's default User model does not provide option to add extra feilds into User Model,
        Creating one class which will store user's extra information by adding PK of USER model as FK
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    mobile = models.CharField(max_length=10)
    profile_picture = models.ImageField(default=None, null=True, blank=True)
    
    """ 
        Return a object representation string. Model Object PK to Category Title. 
        example UserProfile Object (1) to User's username 
    """
    def __str__(self):
        return str(self.user)