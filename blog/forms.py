from django import forms
class SearchForm(forms.Form):
    searchbox = forms.CharField(max_length=100)
    
    