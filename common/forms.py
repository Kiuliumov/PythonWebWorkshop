from django import forms

from common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 40,
                'rows': 4,
                'placeholder': 'Add comment...',
                'maxlength': '250',
                'required': True,
                'id': 'id_text',
            })
        }

