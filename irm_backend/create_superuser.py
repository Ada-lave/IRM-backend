import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'irm_backend.settings')
django.setup()

User = get_user_model()

if not User.objects.filter(username='root').exists():
    User.objects.create_superuser('root', 'root@example.com', 'root')