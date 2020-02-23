from django import forms
from .models import Memos
from .models import Contact

# permet de creer un formulaire a partir du modele

class MemosForm(forms.ModelForm):
	class Meta:
		model = Memos
		fields = '__all__'

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields='__all__'
		

#class ContactForm(forms.Form):
#    sujet = forms.CharField(max_length=100)
#    texte = forms.CharField(widget=forms.Textarea)
#    envoyeur = forms.EmailField(label="Votre adresse e-mail")
#    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)