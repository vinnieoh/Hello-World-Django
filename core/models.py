from django.db import models

# Create your models here.
class UsuarioModel(models.Model):
    email = models.EmailField(max_length=250, blank=False)
    password = models.CharField(max_length=250, blank=False)

    class Meta:
      verbose_name = 'Usuario'
      verbose_name_plural = 'Usuarios'
      ordering = ['id']

    def __str__(self) -> str:
      self.email