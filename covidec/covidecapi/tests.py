from django.test import TestCase

import os
import sys
path = "/Users/roger/Documents/proyectos/repository/djreact/backend/covidec"
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","covidec.settings")

from django.utils import timezone
import django
django.setup()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from covidecapi.models import Pais,CasoCovid,Provincia
from covidecapi.serializers import PaisSerializer,CovidSerializer,ProvinciaSerializer
paiss = Pais.objects.only('codigo').get(codigo="EC")
# print(paiss.codigo)
provincia = Provincia.objects.only('codigo').get(codigo="PICH")

covid = CasoCovid(fk_pais = paiss,fk_provincia = provincia,fecha=timezone.now(),confirmados=500,recuperados=8,muertos=2,activos=5,nuevos=3,total=10)
# covid.save()
# print(covid)
serializer = CovidSerializer(covid)
# print(repr(serializer))
print(serializer.data)
# print("CONTENT=====")
# print(Pais.objects.all())