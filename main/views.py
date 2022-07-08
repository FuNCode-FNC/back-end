from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentForm
from .models import Comment,Film


def main_page(request):
    return render(request, 'main/main_page.html')


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'main/filmpage.html', {'film': film})


def comment_detail(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.Commment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.rating = form.cleaned_data['rating']
                comment.save()
                return redirect('')
    form = CommentForm()
    return render(request, 'main/filmpage.html', {'form': form})