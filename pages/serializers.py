from rest_framework import serializers
from .models import Parent, Child

class ChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Child
        fields = ['name', 'createdAt', 'updatedAt', 'pai', 'mae']
        # depth = 1

class ParentSerializer(serializers.ModelSerializer):
    pai = serializers.PrimaryKeyRelatedField(queryset=Child.objects.all(), many=True)
    # children = ChildSerializer(many=True, read_only=True)
    # pai = ChildSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = ['name', 'createdAt', 'updatedAt', 'pai']
        depth = 1