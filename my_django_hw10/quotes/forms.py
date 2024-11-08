from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Quote


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=35, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):

    quote = CharField(min_length=10, max_length=550, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']
