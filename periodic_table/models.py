from django.db import models

class Element(models.Model):
    atomic_number = models.IntegerField()
    element = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    atomic_mass = models.DecimalField(max_digits=10, decimal_places=5)
    number_of_neutrons = models.IntegerField()
    number_of_protons = models.IntegerField()
    number_of_electrons = models.IntegerField()
    period = models.IntegerField()
    group = models.IntegerField()
    phase = models.CharField(max_length=20)
    radioactive = models.BooleanField()
    natural = models.BooleanField()
    metal = models.BooleanField()
    nonmetal = models.BooleanField()
    metalloid = models.BooleanField()
    types= models.CharField(max_length=20)
    atomic_radius = models.DecimalField(max_digits=6, decimal_places=2)
    electronegativity = models.DecimalField(max_digits=4, decimal_places=2)
    first_ionization = models.DecimalField(max_digits=6, decimal_places=2)
    density = models.DecimalField(max_digits=8, decimal_places=2)
    melting_point = models.DecimalField(max_digits=8, decimal_places=2)
    boiling_point = models.DecimalField(max_digits=8, decimal_places=2)
    number_of_isotopes = models.IntegerField()
    discoverer = models.CharField(max_length=50)
    year = models.IntegerField()
    specific_heat = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_shells = models.IntegerField()
    number_of_valence = models.IntegerField()

    def __str__(self):
        return f"{self.symbol} - {self.element}"


