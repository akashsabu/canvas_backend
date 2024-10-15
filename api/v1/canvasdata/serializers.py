from rest_framework import serializers
from canvas_data.models import CanvasData

class CanvasDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanvasData
        fields = ['id', 'title', 'file', 'image', 'uploaded_at']

    def create(self, validated_data):
        
        user = self.context['request'].user  
        return CanvasData.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
       
        instance.title = validated_data.get('title', instance.title)
        instance.file = validated_data.get('file', instance.file)
        instance.image = validated_data.get('image', instance.image)
        instance.save()  
        return instance
