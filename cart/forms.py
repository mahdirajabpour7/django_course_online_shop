from django import forms


class AddToCart(forms.Form):
    C_Q = [(i , str(i)) for i in range(1 , 30)]


    quantity = forms.TypedChoiceField(choices=C_Q , coerce=int)

    inplase = forms.BooleanField(required=False, widget=forms.HiddenInput)


