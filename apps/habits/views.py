from rest_framework import viewsets, permissions
from .models import Habit
from .serializers import HabitSerializer

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    # Exigimos que el usuario haya iniciado sesión (o enviado un token)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtro de seguridad: El usuario solo ve los hábitos que le pertenecen
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Al crear el hábito, le inyectamos automáticamente el usuario que hizo la petición
        serializer.save(user=self.request.user)