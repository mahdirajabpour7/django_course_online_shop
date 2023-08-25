from django import forms


from .models import  Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body" , "stars" , ]





class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)

