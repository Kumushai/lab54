from django import forms
from django.forms import widgets

from webapp.models import Product


# class SearchForm(forms.Form):
#     product_title = forms.CharField(label="Название товара", required=False)

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class ProductForm(forms.ModelForm):
    balance = forms.IntegerField(min_value=0, label="Остаток")

    class Meta:
        model = Product
        fields = ["title", "price", "balance", "image", "category", "description"]
        widgets = {"description": widgets.Textarea(attrs={"cols": 30, "rows": 5})}
        error_messages = {"title": {"required": "Поле обязательное"}}

