from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True, blank=False)

    def __str__(self):
        return f"{self.nome} <{self.id}>"

    @classmethod
    def cria_categoria(cls, nome):
        if not nome:
            raise ValueError("Categoria deve ter um nome")
        else:
            categoria = Categoria(nome=nome)
            
        categoria.save()
        return categoria

class Evento(models.Model):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    data = models.DateField(null=True)
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome}"

    @classmethod
    def cria_evento(cls, nome, categoria, local=None, link=None, data=None):
        if local:
            if link:
                raise ValueError("Evento não pode possuir local e link.")
            else:
                evento = Evento(nome=nome, categoria=categoria, local=local, data=data)
        else:
            if link:
                evento = Evento(nome=nome, categoria=categoria,link=link, data=data )
            else:
                evento = Evento(nome=nome, categoria=categoria)
        
        evento.save()
        return evento