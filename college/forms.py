from django import forms
from college.models import Webpage, Contact
class ContactForm(forms.Form):
    name = forms.CharField(label='sr-only',widget=forms.TextInput(
    attrs = {'placeholder':'Name','class':'form-control','id':'c_name'}))
    
    email = forms.EmailField(label='sr-only', widget=forms.TextInput(
    attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id':'c_email'}),
    required=False)
    
    message = forms.CharField(label='sr-only', widget=forms.TextInput(
    attrs={'placeholder': 'Message', 'class': 'form-control', 'id':'c_message'}))
    
    
class Form(forms.Form):
    class Meta:
        model = Webpage
        fields = ["Username","types","email","phone","message"]
        
        
        
class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name","email","number","message",)
        
