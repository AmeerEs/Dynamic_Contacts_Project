from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_updated')
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=1)


