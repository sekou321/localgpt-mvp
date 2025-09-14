from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'description', 'category', 'region']
        # On ajoute Bootstrap aux widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Appliquer la classe 'form-control' à tous les champs
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ in ['TextInput', 'Textarea', 'Select']:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label
                })
