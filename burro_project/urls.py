from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar 'path' y 'include'
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


# Vista básica para la ruta raíz
def home(request):
    return HttpResponse("<h1>Bienvenido a la API de Burro</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('burro_api.urls')),
    path('', home),  # Vista para la ruta raíz
]

# El resto de tu configuración sigue igual
try:
    schema_view = get_schema_view(title='Burro API')
    urlpatterns += [
        path('docs/', include_docs_urls(title='Burro API')),
        path('schema/', schema_view),
    ]
except ImportError:
    print("Warning: coreapi not installed, API docs won't be available")
