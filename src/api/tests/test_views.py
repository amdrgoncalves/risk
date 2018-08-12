import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Risk,RiskField
from api.serializers import Risk1Serializer,RiskAllSerializer


# initialize the APIClient app
client = Client()


class GetAllRisksTest(TestCase):
    """ Test module for GET all risks API """

    def setUp(self):
        self.auto = Risk.objects.create(name='Automobile').pk
        Risk.objects.create(name='House')
        Risk.objects.create(name='Prize')


    def test_get_all_risks(self):
        # get API response
        response = client.get(reverse('get_risks'))
        # get data from db
        risks = Risk.objects.all()
        serializer = RiskAllSerializer(risks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_1_risks(self):
        RiskField.objects.create(risk_id=self.auto, caption = 'Name', type='T')
        RiskField.objects.create(risk_id=self.auto, caption = 'BirthDate', type='D')
        RiskField.objects.create(risk_id=self.auto, caption = 'Age', type='N')
        RiskField.objects.create(risk_id=self.auto, caption = 'Gender', type='E',options=['M','F'])
        # get API response
        response = client.get(reverse('get_risk_type',args=[self.auto]))
        # get data from db
        auto_risk = Risk.objects.filter(pk=self.auto)
        serializer = Risk1Serializer(auto_risk, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



        #
