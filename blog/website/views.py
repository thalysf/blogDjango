from django.shortcuts import render
from .models import Post, Contact
def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html', 'Css', 'Banco de dados']
    list_posts = Post.objects.filter(deleted=False)
   # list_posts = Post.objects.all() 
    data = {'name': 'Blog Django', 
            'lista_tecnologias': lista,
            'posts': list_posts}
 
    
    return render(request, 'index.html', data)

def post_detail(request, id):
        post = Post.objects.get(id=id)
        return render(request, 'post_detail.html', {'post': post})

def save_form(request):
        Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message']
                )
        return render(request, 'contact_sucess.html', {'name_contact': request.POST['name']})

