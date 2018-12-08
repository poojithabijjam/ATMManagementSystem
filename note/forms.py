from django.forms import ModelForm
# from .models import note
from django import forms

from note.models import carddet


class carddetForm(forms.ModelForm):
    class Meta:
        model = carddet
        fields = ("cardnum", "pin")
    pin = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Enter New pin'}),
    )
    cardnum = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter cardnum'}),
    )


class login_form(forms.ModelForm):
    class Meta:
        model = carddet
        fields = ("cardnum", "pin")
    pin = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Enter pin'}),
    )
    cardnum = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter cardnum'}),
    )


class deposit_form(forms.ModelForm):
    class Meta:
        model = carddet
        fields = ("balance", )
    balance = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'width': '10',
                                      'placeholder': 'Amount to be deposited'}),
    )

class withdraw_form(forms.ModelForm):
    class Meta:
        model = carddet
        fields = ("cardnum", "balance")
    balance = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'width': '10',
                                      'placeholder': 'Amount to be withdrawled'}),
    )
    cardnum = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'readonly': 'true'}),
    )


class enquire_form(forms.ModelForm):
    class Meta:
        model = carddet
        fields = ("cardnum", "balance")
    balance = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'readonly': 'true'}),
    )
    cardnum = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'readonly': 'true'}),
    )
# class ministatement_form(forms.ModelForm):
#     class Meta:
