from rest_framework import serializers
from .models import SchoolID, NationalID

class SchoolIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolID
        fields = ['id', 'identifier', 'description', 'is_returned', 'found_by', 'lost_by', 'created_at', 'updated_at', 'photo']
        extra_kwargs = {
            'found_by': {'read_only': True},
            'lost_by': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }

class NationalIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalID
        fields = ['id', 'identifier', 'description', 'is_returned', 'found_by', 'lost_by', 'created_at', 'updated_at', 'photo']
        extra_kwargs = {
            'found_by': {'read_only': True},
            'lost_by': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }
