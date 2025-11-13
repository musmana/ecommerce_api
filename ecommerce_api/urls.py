from django.contrib import admin
from django.urls import path, include     # <-- YOU FORGOT THIS EARLIER
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "E-commerce API is running!",
        "endpoints": {
            "categories": "/api/categories/",
            "products": "/api/products/"
        }
    })

urlpatterns = [
    path('', home),   
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
]
