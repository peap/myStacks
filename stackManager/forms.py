from django import forms
from stackManager.models import Collection


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection

