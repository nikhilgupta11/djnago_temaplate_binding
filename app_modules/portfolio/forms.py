from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = "__all__"
        exclude = ["unread"]

        labels = {
            "name": "Full Name",
            "email": "Email",
            "subject": "Subject",
            "message": "Your Message",
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        }