from django import forms

from petstagram.common.models import PhotoComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'placeholder': 'Add comment...',
                'cols': 40,
                'rows': 10
                                                  })
        }