from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Groupetontine
from .models import Membre



def home(request):
    return render(request, "Pages/index.html")
 
def about(request):
    return render(request, "Pages/about.html")

@login_required(login_url="/login/")
def tontine_list(request):
    tontines = Groupetontine.objects.all()
    return render(request, "tontines/new_tontine.html", {"tontines":tontines})


@login_required(login_url="/login/")
def tontine_details(request, id):
    tontine = get_object_or_404(Groupetontine, id=id)
    return render(request, "tontines/tontine_detail.html",{"tontine":tontine})


@login_required(login_url="/login/")
def  new_tontine(request):
     if request.method == "POST":
        nom = request.POST['nom']
        cotisation_amount = request.POST['cotisation_amount']
        frequence_paiement = request.POST['frequece_paiement']
        description = request.POST['description']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        tontine = Groupetontine.objects.Create(
            nom=nom,
            cotisation_amount=cotisation_amount,
            frequece_paiement=frequence_paiement,
            description=description,
            date_debut=date_debut,
            date_fin=date_fin,
        )

        tontine.save()
     return redirect("/tontines/")
     return render (request, "tontines/new_tontine.html")



def edit_tontine(request, id):
    return render(request, "tontines/edit_tontine.html")




def membre_list(request):
        membres = Membre.objects.all()
        return render(request, "tontines/membre_list.html", {"membres":membres})

