from django.urls import path
from . import views

urlpatterns = [
    path("",views.table,name = "table"),
    path("table/details/<int:atomic_number>",views.details,name = "details")
]
