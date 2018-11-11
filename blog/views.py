from django.shortcuts import render, get_object_or_404
from .models import Post #.modelsにすると、model.pyのPostクラスを引っ張れる
                         #.model.py と views.pyは同じファイルにあるため、「.」を入れるだけで、ディレクトリを移動できる
from django.utils import timezone
from .form import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.all() #クエリメソッド
    return render(request, 'blog/post_list.html', {'posts': posts}) #posts辞書を作っている


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})