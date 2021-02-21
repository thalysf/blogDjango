from django.contrib import admin
from .models import Post



# Registra modulos para aparecer no admin 

# Modificando layout de exibição dos posts em /admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'deleted'] # listagem de posts
    search_fields = ['title', 'sub_title'] # tornando os elementos buscáveis

    def get_queryset(self, request):
        return Post.objects.filter(deleted=False)
admin.site.register(Post, PostAdmin)