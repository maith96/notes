from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    item_type = serializers.CharField(source='content_type.model')
    item_id = serializers.UUIDField(source='object_id')

    class Meta:
        model = Transaction
        fields = ['id', 'initiated_by', 'item_type', 'item_id', 'amount', 'phone_number', 'transaction_date', 'updated_at']
        read_only_fields = ['initiated_by']

    def create(self, validated_data):
        validated_data['initiated_by'] = self.context['request'].user
        item_type = validated_data.pop('content_type')['model']
        item_id = validated_data.pop('object_id')
        
        # Fetch the content type based on the model name
        content_type = ContentType.objects.get(model=item_type)
        
        # Create the Transaction instance
        transaction = Transaction.objects.create(
            content_type=content_type,
            object_id=item_id,
            **validated_data
        )
        return transaction
