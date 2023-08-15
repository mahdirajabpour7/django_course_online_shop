from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "phone_number", "address","order_notes",]
        widgets = {
            "address": forms.Textarea(attrs={'placeholder':"در صورتی که نکته ای دارید «هن را اینجا یادداشت کنید......"}),
        }



