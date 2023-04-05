from django.urls import path
from staff.views import inicio, index


urlpatterns = [
    path('', inicio, name="inicio"),
    path('index/', index, name="index")
]
