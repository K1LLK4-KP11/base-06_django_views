from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView  
from django.views.generic import ListView  




class post_list(ListView):  
    model = Post  
    template_name = 'posts/list.html'  
    context_object_name = 'posts'


class post_detail(DetailView):  
    model = Post  
    template_name = 'posts/detail.html'  


# Create your views here.
def error_404(request, exception):
    return render(request, '404.html', status=404) 

def error_500(request):
    return render(request, '505.html', status=500)




from django.views.generic.edit import FormView  
from .forms import PostForm  
from django.contrib.auth.decorators import login_required  

@login_required  
class PostCreateView(FormView):  
    template_name = 'posts/create.html'  
    form_class = PostForm  
    success_url = '/posts/'  

    def form_valid(self, form):  
        form.save()  
        return super().form_valid(form) 