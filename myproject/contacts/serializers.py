from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.version += 1
        instance.save()
        return super().update(instance, validated_data)