from django.db import models

# declare a new model with a name 
class PersonDetailsModel(models.Model):
# fields of the model
	Name = models.CharField(max_length = 200)
	Age = models.IntegerField()
	description = models.TextField()
	last_modified = models.DateTimeField(auto_now_add = True)

	# renames the instances of the model
	def __str__(self):
		return self.Name


class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add = True)

	# renames the instances of the model
	def __str__(self):
		return self.title