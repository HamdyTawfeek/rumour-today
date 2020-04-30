from django import forms

class ContactForm(forms.Form):
    '''
    Email contact form 
    '''
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    sender = forms.EmailField(required=True)
    recipient = forms.EmailField(required=True)