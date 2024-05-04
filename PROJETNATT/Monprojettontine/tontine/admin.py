from django.contrib import admin
from .models import User
from .models import Groupetontine
from .models import Membre
from .models import Paiement
from .models import Contribution






# Register your models here.


#admin.site.register(User)
@admin.register(User)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'adresse', 'telephone', 'motdepasse', 'date_enregistrement')
#admin.site.register(Groupetontine)
@admin.register(Groupetontine)
class GroupetontineAdmin(admin.ModelAdmin):
    list_display = ('nom', 'cotisation_amount', 'frequence_paiement', 'date_creation', 'date_debut')
#admin.site.register(Membre)
@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'groupe_tontine')
#admin.site.register(Paiement)
@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('membre', 'montant', 'date_paiement')
#admin.site.register(Contribution)
@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('montant_contribution', 'date_contribution', 'utilisateur_id', 'groupe_tontine')