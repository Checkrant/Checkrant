
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['data', 'content']
        labels = {
            'data': 'Data',
            'comment': 'Comentario',
        }
        widgets = {
            'data': forms.DateInput(format=('%m/%d/%Y'), attrs={'type': 'date', 'min': '1978-01-01', 'max': '2050-12-31', 'class': 'form-control', 'required': True}),
            'comment': forms.Textarea(attrs={'class': 'descricao', 'placeholder':'Insira um comentario sobre essa avaliacao.', 'required': True, 'minlength': '0', 'maxlength': '500'})
        }