from django.contrib import admin
from models import Usuario, Nota, Produto, Mercado

modelos = [Usuario, Nota, Produto, Mercado]
admin.site.register(modelos)
