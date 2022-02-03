from django.urls import path
from .import views
urlpatterns = [
    path('abc/',views.sample1),
    path('cde/',views.sample2),
    path('efg/',views.sample3)
    ]