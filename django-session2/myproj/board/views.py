from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
  posts = Post.objects.all
  return render(request, 'index.html', {'posts':posts})

def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)

    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('home')

  else:
    form = PostForm()
  return render(request, 'post_new.html', {'form':form})


def post_detail(request, index):
  post = get_object_or_404(Post, pk=index)
  comment_list = Comment.objects.filter(post = post)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.author = request.user
      comment.post = post
      comment.save()
      return redirect('post_detail', index=index)

  else:
    form = CommentForm()
  return render(request, 'post_detail.html', 
  {'post':post, 'form':form, 'comment_list':comment_list})



def post_edit(request, index):
  post = get_object_or_404(Post, pk=index)
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.post_time = timezone.now()
      post.save()
      return redirect('post_detail', index=post.pk)

  else:
    form = PostForm(instance=post)
  return render(request, 'post_edit.html', {'form':form})



def post_delete(request, index):
  post = get_object_or_404(Post, pk=index)
  post.delete()
  return redirect('home')