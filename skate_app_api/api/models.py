from django.db import models

# Create your models here.
# Place 
# this can be a city of a place in the world
class Place(models.Model):

	name = models.CharField(max_length = 500)

	# Get name of objetc
	def __str__(self):

		return self.name


# Location
class Location(models.Model):

	name = models.CharField(max_length = 500)
	latitude = models.DecimalField(max_digits=30, decimal_places=15)
	longitude = models.DecimalField(max_digits=30, decimal_places=15)

	# Place 
	# place = models.ForeignKey(Place, on_delete = models.CASCADE)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)

	# Metodo para obtener nombre de objeto
	def __str__(self):
	   return self.name + '_' + self.place.name

# Videos of location
class Videos_Location(models.Model):

	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	link = models.CharField(max_length = 100000)
	votes = models.IntegerField(default = 0)
	comment = models.CharField(max_length = 2000, null=True)
	activate = models.BooleanField(default = True)

	# It must to be linked to other model (maybe users must to create its own account)
	skater = models.CharField(max_length = 1000)
	# Metodo para obtener nombre de objeto
	def __str__(self):

	   return self.location.name + '_' + self.location.place.name