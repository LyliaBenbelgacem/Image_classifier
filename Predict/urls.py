from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('',views.predict, name = "predict" )

]

urlpatterns += staticfiles_urlpatterns()
