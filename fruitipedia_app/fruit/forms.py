from django import forms

from fruitipedia_app.core.utils import DisableFields
from fruitipedia_app.fruit.models import FruitModel


class BaseFruitForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Fruit Name'}))
    image = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Fruit Description'}))
    nutrition = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Nutrition Info'}))

    class Meta:
        model = FruitModel
        fields = "__all__"


class CreateFruitForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    name = forms.CharField(label="Name:")
    image = forms.CharField(label="Image URL:")
    description = forms.CharField(label="Description:", widget=forms.Textarea({'placeholder': 'Fruit Description'}))
    nutrition = forms.CharField(label="Nutrition:", widget=forms.Textarea({'placeholder': 'Nutrition Info'}))


class DeleteFruitForm(DisableFields, forms.ModelForm):
    name = forms.CharField(label="Name:")
    image = forms.CharField(label="Image URL:")
    description = forms.CharField(label="Description:", widget=forms.Textarea())

    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = FruitModel
        fields = ('name', 'image', 'description')

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
