from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.CharField('Usuário:', max_length=15)
    title = models.CharField('Nome do Livro:', max_length=200)
    image = models.ImageField('Upload da Imagem:', null=True, blank=True)
    text = models.TextField('Descrição:', max_length=1000)
    published_date = models.DateTimeField('Data de Publicação:', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
