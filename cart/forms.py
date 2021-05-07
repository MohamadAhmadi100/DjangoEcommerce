from django import forms
from shop.models import Product


class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, label='',
                                  widget=forms.NumberInput(attrs={'placeholder': 'تعداد', 'class': 'form-control'}))
