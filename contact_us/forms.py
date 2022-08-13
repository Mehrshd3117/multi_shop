from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        # Special widgets
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter your name"
            }),
            "subject": forms.TextInput(attrs={
                "placeholder": "Enter your subject..."
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Enter your message..."
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Please enter the valid email..."
            })
        }

        # Widget for all

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
