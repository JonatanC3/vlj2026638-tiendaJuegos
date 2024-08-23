from django import forms
from .models import Videogame, Order

class VideogameForm(forms.ModelForm):
    class Meta:
        model = Videogame
        fields = ['title', 'release_date', 'genre', 'developer', 'platform', 'description', 'price']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Título',
            'release_date': 'Fecha de Lanzamiento',
            'genre': 'Género',
            'developer': 'Desarrollador',
            'platform': 'Plataforma',
            'description': 'Descripción',
            'price': 'Precio',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        labels = {
            'quantity': 'Cantidad',
        }