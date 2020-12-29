from django import forms

from .models import Message


class ContactModelForm(forms.ModelForm):
    """Form for the contact model."""

    def __init__(self, *args, **kwargs):
        super(ContactModelForm, self).__init__(*args, **kwargs)

        # Override attributes of the auto-generated fields
        self.fields['name'].required = False
        self.fields['content'].widget.attrs['placeholder'] = 'Write here your message...'

    class Meta:
        model = Message
        fields = '__all__'
