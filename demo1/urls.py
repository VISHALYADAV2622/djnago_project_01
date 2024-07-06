"""
import  demo1 views  and create a path to endpoint of  urls 

"""


from django.urls import path
from .import views

"""
define urls in urlpatters

"""
urlpatterns = [
    path("home/",views.home,name="home"),
    path("about/",views.about,name="about"), 

]
