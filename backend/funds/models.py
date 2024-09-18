import uuid
from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    initiated_by = models.ForeignKey('api.CustomUser', on_delete=models.CASCADE, related_name='transactions')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()  # Assuming UUIDs are used as primary keys
    item = GenericForeignKey('content_type', 'object_id')    
    amount = models.FloatField(default=0.0)
    phone_number = models.TextField(max_length=13)
    
    transaction_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Transaction for {self.item} by {self.user}"