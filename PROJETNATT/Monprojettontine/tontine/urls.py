from django.urls import path
from .views import home, about, tontine_list, tontine_details, new_tontine,membre_list, edit_tontine

urlpatterns = [
    path("", home, name="index"),
    path("about/", about, name="about"),
    path("tontines/", tontine_list, name="tontines"),
    path("membres/", membre_list, name="membres"),
    path("tontines/new/", new_tontine, name="new_tontine"),
    path("tontines/<int:id>/", tontine_details, name="details"),
    path("tontines/edit/<int:id>/", edit_tontine, name="edit_tontine"),

    

]