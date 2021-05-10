from django.urls import path
from testapp import views
urlpatterns = [
    path('', views.index, name = "index"),
    path('runcode', views.runcode, name = "runcode"),
]
