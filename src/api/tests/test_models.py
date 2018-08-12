from django.test import TestCase
from ..models import Risk,RiskField
from django.core.exceptions import ValidationError


class RiskTest(TestCase):
    """ Test module for Risk model """

    def setUp(self):
        self.r = Risk.objects.create(
            name='Automobile')

    def test_standard_insert(self):
        #All commum inserts work as expected.
        r = RiskField(risk=self.r, caption = 'Name', type='T')
        r.save()
        self.assertEqual(r.caption, 'Name')
        r = RiskField(risk=self.r, caption = 'BirthDate', type='D')
        r.save()
        self.assertEqual(r.caption, 'BirthDate')
        r = RiskField(risk=self.r, caption = 'Age', type='N')
        r.save()
        self.assertEqual(r.caption, 'Age')
        r = RiskField(risk=self.r, caption = 'Gender', type='E',options=['M','F'])
        r.save()
        self.assertEqual(r.caption, 'Gender')

        #Only pre-defined choices of fields should be saved.
        with self.assertRaises(ValidationError):
            RiskField(risk=self.r, caption = 'Gender', type='W').save()

    def test_num_validation(self):
        #For type enum, we expect an options key argument.
        with self.assertRaises(ValidationError):
            RiskField(risk=self.r, caption = 'Gender', type='E').save()
        #For other types, the options argument shouldn't be defined
        with self.assertRaises(ValidationError):
            RiskField(risk=self.r, caption = 'Name', type='T',options=['A','B']).save()
