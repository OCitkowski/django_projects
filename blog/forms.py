from django import forms
from .models import Tag


class PostsChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
