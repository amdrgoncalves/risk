from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError


class Risk(models.Model):
    name = models.CharField(max_length=30)

class RiskField(models.Model):
    TYPE_CHOICES = (
        ('E','ENUM'),
        ('N', 'NUM'),
        ('T','TEXT'),
        ('D','DATE'),
    )
    risk = models.ForeignKey('Risk',related_name='risk_field',on_delete=models.CASCADE)
    caption = models.CharField(max_length=30)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    options = ArrayField(models.CharField(max_length=20),null=True)

    def save(self, *args, **kwargs):
        #Custom validation
        error1 = self.type == 'E' and not self.options
        error2 = self.type != 'E' and self.options
        error3 = self.type not in [x[0] for x in self.TYPE_CHOICES]
        if error1:
            raise ValidationError('Choice field needs at list two options')
        elif error2:
            raise ValidationError('No options allowed for non enum field')
        elif error3:
            raise ValidationError('Type not valid')
        else:
            super(RiskField, self).save(*args, **kwargs)
