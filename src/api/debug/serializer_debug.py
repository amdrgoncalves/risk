import os
import sys
import django
from api.models import *
from api.serializers import *


sys.path.append("/src")
os.environ["DJANGO_SETTINGS_MODULE"] = "risk.settings"
django.setup()

r = Risk.objects.filter(pk=1)
s = Risk1Serializer(r, many=True)
print(s.data)
