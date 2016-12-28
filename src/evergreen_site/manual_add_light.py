import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evergreen_site.settings')

import django
django.setup()

from lights.models import Light

def add(ipAddress, name, autoOffTime):
	light = Light.objects.get_or_create(name=name, ipAddress=ipAddress, autoOffTimeSeconds=autoOffTime)[0]
	light.save()

if __name__ == '__main__':
	add("192.168.1.112", "Basement Back Room", 60)