from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import PostModel,Comment
from . forms import PostModelForm,PostUpdateForm,CommentForm
@login_required
def index(request):
    context={}
    data=PostModel.objects.all().order_by('-id')
    if request.method=='POST':
        forms = PostModelForm(request.POST)
        if forms.is_valid():
            instance=forms.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('index-page')
    else:
        forms = PostModelForm()
        context = {
            'data': data,
            'forms': forms
        }
    return render(request,'post/index.html',context)


def post_detail(request,pk):
    post=PostModel.objects.get(id=pk)
    if request.method=='POST':
        c_form=CommentForm(request.POST)
        if c_form.is_valid():
            instance=c_form.save(commit=False)
            instance.post=post
            instance.user=request.user
            instance.save()
            return redirect('post-detail-page',pk=post.id)
    else:
        c_form=CommentForm()
    context={
        'post':post,
        'c_form':c_form
    }
    return render(request,'post/post_detail.html',context)

def post_edit(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method=='POST':
        form=PostUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail-page',pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form':form
    }
    return render(request, 'post/post_edit.html', context)


def post_delete(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('index-page')
    context = {
        'post': post
    }
    return render(request,'post/post_delete.html',context)