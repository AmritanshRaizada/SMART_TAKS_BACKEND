from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="amritansh").exists():
            User.objects.create_superuser(
                username="amritansh",
                password="amrit",
                email="admin@example.com"
            )
            print("🛡️ Superuser 'amritansh' created.")
        else:
            print("✅ Superuser already exists.")
