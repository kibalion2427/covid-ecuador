from django.db import models



class Provincia(models.Model):
    codigo = models.CharField(max_length=25,primary_key=True,null=False,unique=True)
    nombre = models.CharField(max_length=50)
    latitud = models.CharField(max_length=25)
    longitud = models.CharField(max_length=25)
    urlImagen= models.CharField(max_length=100)
    # casos = models.ManyToManyField(CasoCovid, through='CasoCovid')

    class Meta:
        db_table = "Provincia"

    def __str__(self):
        return self.codigo

class Pais(models.Model):
    codigo = models.CharField(max_length=25,primary_key=True,null=False,unique=True)
    # confirmados = models.DecimalField(max_digits=None,decimal_places=10)
    nombre = models.CharField(max_length=50)
    latitud = models.CharField(max_length=25)
    longitud = models.CharField(max_length=25)
    urlImagen= models.CharField(max_length=100)
    # provincias = models.ManyToManyField(Provincia, related_name='pvs')

    class Meta:
        db_table = "Pais"


    def __str__(self):
        return self.codigo

class CasoCovid(models.Model):
    fk_pais = models.ForeignKey(Pais,on_delete=models.CASCADE,related_name='paises')
    fk_provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE,related_name='provincias')
    fecha = models.DateTimeField("date published",auto_now=False)
    confirmados = models.FloatField(blank=True,null=True)
    recuperados = models.FloatField(blank=True,null=True)
    muertos = models.FloatField(blank=True,null=True)
    activos = models.FloatField(blank=True,null=True)
    nuevos = models.FloatField(blank=True,null=True)
    total = models.FloatField(blank=True,null=True)

    class Meta:
        db_table = "CasoCovid"

    def __str__(self):
        return str(self.fecha)
        # return str(self.fk_pais) + "|" + str(self.fk_provincia) + "|" + str(self.fecha) + "|" + str(self.total)

