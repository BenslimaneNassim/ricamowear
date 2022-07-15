from django.forms import ModelForm, widgets
from .models import Commande
from django import forms

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
        exclude = ['product','size','date','wilaya','selled']
        widgets = {
            'nom' : forms.TextInput(attrs={'placeholder':'Nom','class':'commande-input'}),
            'prénom' : forms.TextInput(attrs={'placeholder':'Prenom','class':'commande-input'}),
            #'wilaya' : forms.TextInput(attrs={'placeholder':'Wilaya','class':'wilaya-input'}),
            'ville' : forms.TextInput(attrs={'placeholder':'Ville','class':'commande-input'}),
            'adresse' : forms.TextInput(attrs={'placeholder':'Adresse','class':'commande-input'}),
            'numero' : forms.TextInput(attrs={'placeholder':'Numero','class':'commande-input'}),
            'optionel' : forms.TextInput(attrs={'placeholder':'Note optionelle ','class':'commande-optionel-input'}),
        }
