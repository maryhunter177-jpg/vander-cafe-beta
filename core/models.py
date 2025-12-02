from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Usuário Personalizado (Produtor, Especialista, Cliente)
class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('CLIENTE', 'Consumidor Final'),
        ('PRODUTOR', 'Cafeicultor'),
        ('ESPECIALISTA', 'Especialista (Vander)'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='CLIENTE')
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True)

# 2. O Café (Produto)
class Cafe(models.Model):
    produtor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='meus_cafes')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='cafes/')
    
    # Link do vídeo da prova (YouTube)
    video_url = models.URLField(blank=True, help_text="Link do vídeo da prova")
    
    STATUS_CHOICES = (
        ('ANALISE', 'Em Análise'),
        ('APROVADO', 'Aprovado na Loja'),
        ('REPROVADO', 'Reprovado'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ANALISE')

    def __str__(self):
        return self.nome