from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
  nom = models.CharField(max_length=100)
  prenom = models.CharField(max_length=100)
  email = models.EmailField(max_length=30, null=True, blank=True)
  motdepasse = models.CharField(max_length=100)
  adresse = models.CharField(max_length=100)
  date_enregistrement = models.DateTimeField(auto_now_add=True)
  telephone = models.CharField(max_length=100)



class Groupetontine(models.Model):
  nom = models.CharField(max_length=100)
  cotisation_amount = models.CharField(max_length=150)
  frequence_paiement = models.CharField(max_length=70)
  date_creation = models.DateTimeField(auto_now_add=True)
  description = models.TextField(max_length=200)
  date_debut = models.DateTimeField()
  date_fin = models.DateTimeField()


class Membre(models.Model):
  utilisateur = models.ForeignKey(User,on_delete=models.CASCADE)
  groupe_tontine = models.ForeignKey(Groupetontine, on_delete=models.CASCADE)
#def __str__(self):
 # return self.utilisateur

class Paiement(models.Model):
  montant = models.DecimalField(max_digits=10, decimal_places=2)
  date_paiement = models.DateTimeField(auto_now_add=True)
  membre = models.ForeignKey(Membre, on_delete=models.CASCADE)

class Contribution(models.Model):
  montant_contribution = models.CharField(max_length=500)
  date_contribution = models.DateTimeField(auto_now_add=True)
  utilisateur_id = models.ForeignKey(User, on_delete=models.CASCADE)
  groupe_tontine = models.ForeignKey(Groupetontine,on_delete=models.CASCADE)










