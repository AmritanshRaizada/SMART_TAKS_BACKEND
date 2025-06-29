from rest_framework import viewsets
from .models import Project, Task, ActivityLog
from .serializers import ProjectSerializer, TaskSerializer, ActivityLogSerializer
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAdminUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Only admin can fetch users


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        log, created = ActivityLog.objects.get_or_create(task=instance)
        log.prev_assignee = instance.assigned_to
        log.prev_status = instance.status
        log.prev_due_date = instance.due_date
        log.save()

class ActivityLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer