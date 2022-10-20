from django.shortcuts import render
from django.views.generic import CreateView
from .models import Comment
from .forms import CommentForm

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = '/#/'