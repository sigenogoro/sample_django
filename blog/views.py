from django.shortcuts import render
from .models import Post #.modelsにすると、model.pyのPostクラスを引っ張れる

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})