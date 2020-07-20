from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def http_response(request):
    return HttpResponse('안녕하세요')


def template_render(request):
    return render(request, 'blog/template_render.html', {
        'name': '이름'
    })


def model_template_render(request):
    post = Post.objects.get(pk=1)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })
