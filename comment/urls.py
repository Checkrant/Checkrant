from django.urls import path
from .views import CommentCreateView

urlpatterns = [

    path('Addcomment/', CommentCreateView.as_view(), name='comment.index'),
]