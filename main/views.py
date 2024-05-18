from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Artwork, Comment
from .forms import CommentForm

def index(requset):
    return render(requset, "main/index.html")

def gallery(request):
    artworks = Artwork.objects.all()
    paginator = Paginator(artworks, 6)  # 페이지당 6개의 작품을 보여주기

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery.html', {'page_obj': page_obj})

def index(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 성공적으로 댓글을 저장한 후 페이지를 새로 고침
    else:
        form = CommentForm()
    
    comments_list = Comment.objects.all().order_by('-created_at')  # 최신 댓글이 먼저 나오도록 정렬
    comment_count = comments_list.count()
    paginator = Paginator(comments_list, 5)  # 페이지당 10개의 댓글을 보여줍니다.
    page_number = request.GET.get('page')
    comments = paginator.get_page(page_number)  # Paginator에서 현재 페이지를 가져옴

    return render(request, 'main/index.html', {'form': form, 'comments': comments, 'comment_count': comment_count})