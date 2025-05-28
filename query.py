#!/usr/bin/env pythonclass Meta:
import os
import django
from ControlAutores.models import Autor
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Biblioteca.settings')
django.setup()

# Método 1: Crear y guardar
'''
autor = Autor(nombre="Gabriel", apellido="García Márquez")
autor.save()
# Método 2: Crear con create()
autor = Autor.objects.create(nombre="Gabriel", apellido="García Márquez")

'''
# Metodo 2: leer
'''
# Obtener todos los registros
autores = Autor.objects.all()

# Obtener un registro por su clave primaria
autor = Autor.objects.get(pk=1)

# Obtener el primer registro que cumpla con ciertos criterios
autor = Autor.objects.filter(apellido="García Márquez").first()

'''

# Metodo 3: Actualizar

'''
# Método 1: Obtener, modificar y guardar
autor = Autor.objects.get(pk=1)
autor.nombre = "Gabriel José"
autor.save()


# Método 2: Actualizar directamente
Autor.objects.filter(pk=1).update(nombre="Gabriel José")

'''

# Metodo 4: Eliminar
'''
# Método 1: Obtener y eliminar
autor = Autor.objects.get(pk=1)
autor.delete()

# Método 2: Eliminar directamente
Autor.objects.filter(apellido="García Márquez").delete()

'''
# Consultas simples
'''
# Filtrar por condición exacta
autores = Autor.objects.filter(apellido="García Márquez")

# Filtrar por múltiples condiciones (AND)
autores = Autor.objects.filter(apellido="García Márquez", nombre="Gabriel")

# Excluir registros
autores = Autor.objects.exclude(apellido="García Márquez")

# Limitar resultados
autores = Autor.objects.all()[:5] # Primeros 5 resultados
autores = Autor.objects.all()[5:10] # Resultados del 6 al 10
'''
# Metodo ordenar
'''
# Ordenar por un campo (ascendente)
autores = Autor.objects.order_by('apellido')

# Ordenar por un campo (descendente)
autores = Autor.objects.order_by('-fecha_nacimiento')

# Ordenar por múltiples campos
autores = Autor.objects.order_by('apellido', 'nombre')

'''
