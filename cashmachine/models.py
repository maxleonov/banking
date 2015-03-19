import hashlib
from django.core.validators import RegexValidator
from django.db import models


PIN_RETRIES_LIMIT = 3

GET_CASH = 'Get cash'
VIEW_BALANCE = 'View balance'

OPERATION_CHOICES = [
    tuple([GET_CASH]*2),
    tuple([VIEW_BALANCE]*2)
]


class Card(models.Model):

    id = models.BigIntegerField(
        primary_key=True,
        validators=[RegexValidator(regex='[0-9]{16}')]
    )
    pin = models.CharField(
        u'PIN', max_length=32,
       validators=[RegexValidator(regex='[0-9]{4}')]
    )
    balance = models.BigIntegerField(default=0)
    blocked = models.BooleanField(default=False)
    pin_attempts_made = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def clean(self):
        if len(self.pin) != 32:
            self.pin = Card.get_pin_hash(self.pin)

    @classmethod
    def get_pin_hash(self, pin):
        return hashlib.md5(pin).hexdigest()


class Operation(models.Model):

    name = models.CharField(u'Name', max_length=50, unique=True, blank=False,
                            choices=OPERATION_CHOICES)

    def __unicode__(self):
        return self.name


class LogRecord(models.Model):

    card = models.ForeignKey(Card)
    operation = models.ForeignKey(Operation)
    created_at = models.DateTimeField()
    amount = models.BigIntegerField(default=None)
    balance_after_operation = models.BigIntegerField(default=None)

