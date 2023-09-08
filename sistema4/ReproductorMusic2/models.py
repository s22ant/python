from django.db import models

class Usuario(models.Model):
    nick = models.CharField(primary_key=True, max_length=20) # campo auto_increment
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45) 
    email = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombre}{self.apellido}"

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    
class Cancion(models.Model):
    id = models.AutoField(primary_key=True)
    genero =  models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    ruta = models.CharField(max_length=200)
    usuario_nick = models.ForeignKey(Usuario, on_delete=models.CASCADE)


 