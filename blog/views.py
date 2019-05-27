from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .formsimport PostForm

def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte = timezone.now())
    qs = qs.order_by('published_date')


    return render(request, 'blog/post_list.html', {
        'post_list': qs, 
    })
def post_new(request) :
    form = PostForm()
    return render(request, 'blog/post_edit.html',{
        'form':form,
    })
    

