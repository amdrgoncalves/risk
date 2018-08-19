from django.test import TestCase
from ..models import Risk, RiskField
from django.core.exceptions import ValidationError


class RiskTest(TestCase):
    """ Test module for Risk model """

    def setUp(self):
        self.r = Risk.objects.create(
            name='Automobile')

    def test_standard_insert(self):
        # All commum inserts work as expected.
        r = RiskField.objects.create(risk=self.r, caption='Name', type='T')
        self.assertEqual(r.caption, 'Name')
        r = RiskField.objects.create(risk=self.r,
                                     caption='BirthDate',
                                     type='D')
        self.assertEqual(r.caption, 'BirthDate')
        r = RiskField.objects.create(risk=self.r, caption='Age', type='N')
        self.assertEqual(r.caption, 'Age')
        r = RiskField.objects.create(risk=self.r,
                                     caption='Gender',
                                     type='E',
                                     options=['M', 'F'])
        self.assertEqual(r.caption, 'Gender')

        # Only pre-defined choices of fields should be saved.
        with self.assertRaises(ValidationError):
            RiskField.objects.create(risk=self.r, caption='Gender', type='W')

    def test_num_validation(self):
        # For type enum, we expect an options key argument.
        with self.assertRaises(ValidationError):
            RiskField(risk=self.r, caption='Gender', type='E').save()
        # For other types, the options argument shouldn't be defined
        with self.assertRaises(ValidationError):
            RiskField(risk=self.r,
                      caption='Name',
                      type='T',
                      options=['A', 'B']).save()
