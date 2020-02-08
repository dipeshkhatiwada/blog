from django import forms
from .models import Blog,Category


class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder':'select category'}))
    class Meta:
        model = Blog
        # fields = ['title', ]
        # exclude = ['title', ]
        fields = '__all__'
