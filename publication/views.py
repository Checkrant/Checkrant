from imp import get_frozen_object
from pdb import Restart
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from users.models import UserRant
from .models import Restaurant, Review
from .forms import ReviewForm
from django.urls import reverse,reverse_lazy


def pub(request):
    items = UserRant.objects.all()
    context = {
        'items':items,
    }
    return render(request, "pub.html", context)

def viewReview(request):
    itemsR = Review.objects.all()
    context = {
        'itemsR':itemsR
    }
    return render(request, "reviews.html", context)

def rate(request, id):
    post = UserRant.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        writer = request.POST.get('writer')
        stars = request.POST.get('stars')
        detail = request.POST.get('detail')
        review = Review(writer=writer, stars=stars,  detail=detail , restaurant=post)
        
        review.save()
        return redirect('success')
    
    form = ReviewForm()
    context = {
        "form":form
    }
    return render(request, 'rate.html',context)

def like_rate(request,pk):
    post=get_object_or_404(Review, id=request.POST.get('rate_id'))
    post.likes.add(request.user)
    return redirect('success')


def success(request):
    return render(request, "success.html")