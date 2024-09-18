import uuid
from django.db import models
import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def get_item_path(instance, filename):
    return os.path.join('items', filename)

def get_school_id_path(instance, filename):
    return os.path.join('items', 'school_ids', filename)

def get_national_id_path(instance, filename):
    return os.path.join('items', 'national_ids', filename)

# Base class for Items
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    identifier = models.CharField(max_length=100)
    description = models.TextField()
    is_returned = models.BooleanField(default=False)
    found_by = models.ForeignKey('api.CustomUser', on_delete=models.CASCADE, related_name='%(class)s_found_items')
    lost_by = models.ForeignKey('api.CustomUser',on_delete=models.SET_NULL, blank=True, null=True, related_name='%(class)s_lost_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Mark as abstract so it's not created in the DB

    def process_image(self, photo):
        img = Image.open(photo)
        img_io = BytesIO()
        img.save(img_io, format='WEBP')  # Save as WebP
        img_content = ContentFile(img_io.getvalue(), name=f"{uuid.uuid4()}.webp")
        return img_content

# Inherited class for School ID
class SchoolID(Item):
    photo = models.ImageField(upload_to=get_school_id_path)
    
    def save(self, *args, **kwargs):
        if self.photo:
            self.photo = self.process_image(self.photo)
        super().save(*args, **kwargs)

# Inherited class for National ID
class NationalID(Item):
    photo = models.ImageField(upload_to=get_national_id_path)
    
    def save(self, *args, **kwargs):
        if self.photo:
            self.photo = self.process_image(self.photo)
        super().save(*args, **kwargs)
