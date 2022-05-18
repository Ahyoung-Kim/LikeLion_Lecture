from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm

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


def detail(request, post_id):
  post = get_object_or_404(Post, pk=post_id)

  return render(request, 'detail.html', 
  {'post':post})