from django.forms import ModelForm, widgets
from .models import Commande, WILAYAS
from django import forms

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
        exclude = ['date','selled','domicile']
        widgets = {
            'nom' : forms.TextInput(attrs={'placeholder':'Nom','class':'commande-input'}),
            'prénom' : forms.TextInput(attrs={'placeholder':'Prenom','class':'commande-input'}),
            'wilaya' : forms.Select( attrs={'class':'wilaya-input'},choices=WILAYAS),
            'ville' : forms.TextInput(attrs={'placeholder':'Ville','class':'commande-input'}),
            'adresse' : forms.TextInput(attrs={'placeholder':'Adresse','class':'commande-input'}),
            'numero' : forms.TextInput(attrs={'placeholder':'Numero','class':'commande-input'}),
            'optionel' : forms.TextInput(attrs={'placeholder':'Note optionelle ','class':'commande-optionel-input'}),
        }
