from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from .forms import ContactForm
from .models import Contact,Post
from django.db.models import Q
# Create your views here.
def home(request):
    print('in home')
    all_posts= Post.objects.all()
    form= contact(request)
    return render(request,'blog/home.html',{'all_posts':all_posts[0:3],'form': form})


def all_posts(request):
    all_posts_all= Post.objects.all()
    return render(request,'blog/all_blog.html',{'all_posts_all':all_posts_all})


def contact(request):
    print('in contact now')
    # form= ContactForm(request.POST)
    if request.method == "POST":
        form= ContactForm(request.POST)
        if form.is_valid():
          form.save()
        #   x.num = form.cleaned_data['num']*3
        #   x.save() play
        #   print(form.cleaned_data['num'])  #getintothedataofform
          return(HttpResponseRedirect('/'))
    else :
        form= ContactForm()
    #return render(request,'blog/forms.html',{'form': form})
    return(form)


def blog_details(request,id):
    single_post = Post.objects.get(id=id)
    return render(request, 'blog/blog_details.html',{'single_post':single_post})



def search(request):
    search_post = request.GET.get('search')
    if search_post:
        post = Post.objects.filter(Q(title__icontains=search_post))
    else :
        pass
    return render(request,'blog/search.html',{'post':post,'size':post.count()})


