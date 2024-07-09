from django.shortcuts import render

from .models import Post, Comment
from .forms import CommentForm
from skillapp.models import Skill
def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'postapp/list.html', {'postlar': posts})


def get_post(request, pk):
    post = Post.objects.get(pk=pk)
    template_name = 'postapp/detail.html'
    comments = post.comments.all()
    tags = post.tags.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = request.POST.get("parentId")
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(pk=parent_id)
            if parent_obj:
                cf = comment_form.save(commit=False)
                cf.parent = parent_obj
                cf.post = post
                cf.save()
                comment_form = CommentForm()
    context = {'post': post, 'comment_form': comment_form, 'comments': comments, 'tags': tags}
    return render(request, template_name, context)


def get_posts_by_tag(request, tag_name):
    filter = True
    template_name = 'postapp/list.html'
    posts = Post.objects.filter(tags__name=tag_name).all()
    context = {'posts': posts, 'filter': filter}

    return render(request, template_name, context)


def about(request):
    skills = Skill.objects.all()
    template_name = 'postapp/about.html'
    context = {'skills': skills}
    return render(request, template_name, context)
