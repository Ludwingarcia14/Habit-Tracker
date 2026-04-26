from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'user', 'name', 'description', 'created_at', 'is_active']
        # Protegemos estos campos para que el usuario no pueda inyectar datos falsos
        read_only_fields = ['id', 'created_at', 'user']