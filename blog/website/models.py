from django.db import models

# Create your models here.

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField(default='')
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
        )
    deleted = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)
    # null=True, blank=True -> torna campo não obrigatório o preenchimento
    
    def __str__(self): # Exibe titulo do post na edição
        return self.title

    def full_name(self):
        return self.title + self.sub_title
    def get_category_label(self):
        return self.get_categories_display()
    full_name.admin_order_field = 'title' #tornando ordenável full_name

    