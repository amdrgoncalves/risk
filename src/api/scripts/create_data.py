import os
import sys
import django
from api.models import *

sys.path.append("/src")
os.environ["DJANGO_SETTINGS_MODULE"] = "risk.settings"
django.setup()

# risk
r = Risk.objects.create(name='Automobile')
r2 = Risk.objects.create(name='House')

<<<<<<< HEAD

#riskfields automobile
=======
# riskfields
>>>>>>> aab1135f8e3ddc5dd2d35a7778893ec76e1031a5
RiskField.objects.create(risk=r, caption='Name', type='T')
RiskField.objects.create(risk=r, caption='BirthDate', type='D')
RiskField.objects.create(risk=r, caption='Age', type='N')
RiskField.objects.create(risk=r,
<<<<<<< HEAD
                         caption='Gender', type='E',
                         options=['M','F'])

# riskfields house
RiskField.objects.create(risk=r2, caption='Address', type='T')
RiskField.objects.create(risk=r2, caption='Number of rooms', type='E',
                            options=['1', '2', '3', '4', '5+'])
=======
                         caption='Gender',
                         type='E',
                         options=['M', 'F'])
>>>>>>> aab1135f8e3ddc5dd2d35a7778893ec76e1031a5
