from django import forms
from .models import Trains

class TrainsForm(forms.ModelForm):
    class Meta:
        model = Trains
        fields = ['depart', 'destination', 'arrets', 'h_depart', 'h_arrivee']
        labels = {
            'depart': 'Départ',
            'destination': 'Destination',
            'arrets': 'Nombre d\'arrêts',
            'h_depart': 'Heure de départ',
            'h_arrivee': 'Heure d\'arrivée',
        }