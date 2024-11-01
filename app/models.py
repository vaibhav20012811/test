from django.db import models

# Create your models here.
class EcomUser(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'ecom_user'
        managed = True