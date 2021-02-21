from django.contrib import admin
from .models import Post, Contact





# Modificando layout de exibição dos posts em /admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'deleted'] # listagem de posts
    search_fields = ['title', 'sub_title'] # tornando os elementos buscáveis

    # Filtrando exibição dos posts em /admin
    #def get_queryset(self, request):
     #   return Post.objects.filter(deleted=False)

# Modificando layout de exibição dos contatos em /admin
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message'] 
    search_fields = ['name']     
    
# Registra modulos para aparecer no admin 
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)