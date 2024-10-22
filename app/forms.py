from django import forms


class HeyForm(forms.Form):
    name = forms.CharField(max_length=100)


class AgeForm(forms.Form):
    end = forms.IntegerField()
    birthyear = forms.IntegerField()


class OrderForm(forms.Form):
    burgers = forms.IntegerField(min_value=0)
    fries = forms.IntegerField(min_value=0)
    drinks = forms.IntegerField(min_value=0)
