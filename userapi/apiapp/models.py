from django.db import models

# user_registration table
class UserProfile(models.Model):
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user_name
    
# warehouse.....
class Warehouse(models.Model):
    whs_code = models.CharField(max_length=255)
    whs_name = models.CharField(max_length=255)
    locCode = models.CharField(max_length=255)
    locked = models.BooleanField(default=False)
    binActivant = models.BooleanField(default=False)
    Brunchno = models.IntegerField()

    def __str__(self):
        return self.whs_name