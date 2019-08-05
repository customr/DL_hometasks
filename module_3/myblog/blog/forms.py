from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Comment:', max_length=150)