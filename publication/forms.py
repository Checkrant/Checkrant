from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["writer","stars","detail"]
        labels = {
            'writer': 'Autor',
            'stars': 'Estrelas',
            'detail': 'Comentário'
        }
