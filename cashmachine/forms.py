from django import forms
from django.core.validators import RegexValidator, MinValueValidator


class CardForm(forms.Form):
    card_id = forms.CharField(
        required=True, max_length=19, initial='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        validators=[RegexValidator(regex='[0-9-]{19}')]
    )


class PinForm(forms.Form):
    pin = forms.CharField(
        required=True, max_length=4, initial='',
        widget=forms.PasswordInput(attrs={'readonly': 'readonly'}),
        validators=[RegexValidator(regex='[0-9]{4}')]
    )


class GetCashForm(forms.Form):
    amount = forms.IntegerField(
        required=True, initial='',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        validators=[RegexValidator(regex='[0-9]{1,20}'),
                    MinValueValidator(1)]
    )
