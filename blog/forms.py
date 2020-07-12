from django import forms
from blog.models import Post,Comments

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author' , 'title' , 'text')

        widgets = {
            'author': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control textinputclass'}),
            'text': forms.Textarea(attrs={'class':'form-control editable medium-editor-text-area postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author' , 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control editable medium-editor-text-area'}),
        }