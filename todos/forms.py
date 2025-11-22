from django import forms
from .models import TODO


class TODOForm(forms.ModelForm):
    """Formulario personalizado para TODO con widgets HTML5"""
    
    class Meta:
        model = TODO
        fields = ['title', 'description', 'due_date', 'resolved']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Ingresa el título del TODO',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descripción detallada (opcional)',
                'rows': 4,
                'class': 'form-control'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'resolved': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'due_date': 'Fecha de vencimiento',
            'resolved': 'Marcar como resuelto'
        }
