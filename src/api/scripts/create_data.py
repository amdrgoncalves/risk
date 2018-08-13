import os
import sys
import django

sys.path.append("/src")
os.environ["DJANGO_SETTINGS_MODULE"] = "risk.settings"
django.setup()

from api.models import *

#risk
r = Risk.objects.create(name='Automobile')
Risk.objects.create(name='House')
Risk.objects.create(name='Travel')

#riskfields
RiskField.objects.create(risk=r, caption = 'Name', type='T')
RiskField.objects.create(risk=r, caption = 'BirthDate', type='D')
RiskField.objects.create(risk=r, caption = 'Age', type='N')
RiskField.objects.create(risk=r,
    caption = 'Gender', type='E',options=['M','F'])
