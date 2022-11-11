from imp import get_frozen_object
from pdb import Restart
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from users.models import UserRant
from .models import Restaurant, Review
from .forms import ReviewForm
from django.urls import reverse, reverse_lazy


def pub(request):
    items = UserRant.objects.all()
    context = {
        'items': items,
    }
    return render(request, "pub.html", context)


def viewReview(request):
    itemsR = Review.objects.all()
    context = {
        'itemsR': itemsR
    }
    return render(request, "reviews.html", context)


def favorite(request):
    itemsF = UserRant.objects.all()
    context = {
        'itemsF': itemsF,
    }
    return render(request, "favorites.html", context)


def rate(request, id):
    post = UserRant.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        writer = request.POST.get('writer')
        stars = request.POST.get('stars')
        detail = request.POST.get('detail')
        review = Review(writer=writer, stars=stars, detail=detail, restaurant=post)

        review.save()
        return redirect('success')

    form = ReviewForm()
    context = {
        "form": form
    }
    return render(request, 'rate.html', context)


def like_rate(request, id):
    post = get_object_or_404(Review, id=id)
    if post.users_likes.filter(id = request.user.id).exists():
        post.users_likes.remove(request.user)
    else:
       post.users_likes.add(request.user)
    return redirect('success')


def success(request):
    return render(request, "success.html")

def add_fav(request, id):
    post = get_object_or_404(UserRant, id=id)
    if post.favorites.filter(id = request.user.id).exists():
        post.favorites.remove(request.user)
    else:
       post.favorites.add(request.user)
    return redirect('success')



