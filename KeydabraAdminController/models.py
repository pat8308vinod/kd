from django.db import models

from AuthenticationService.models import Role, UserCredentials

# Create your models here.
class KeydabraUser(models.Model):
    ID = models.ForeignKey(UserCredentials, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    isActive = models.BooleanField(null=True)
    roleID = models.ForeignKey(Role, default=1, on_delete=models.CASCADE, db_column='roleID')
    createdDate = models.DateTimeField(null=True)
    updatedDate = models.DateTimeField(auto_now_add=True)
    designation = models.CharField(max_length=20)

    class Meta:
        db_table = 'KeydabraUser'