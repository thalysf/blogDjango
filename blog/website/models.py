from django.db import models

# Create your models here.

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

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
    # Exibe titulo do post na edição
    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

    full_name.admin_order_field = 'title' #tornando ordenável full_name

    