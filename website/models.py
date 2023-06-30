from django.db import models

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	mess_name = models.CharField(max_length=50)
	mess_menu =  models.CharField(max_length=250)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	price=models.CharField(max_length=3,default='90')

	
	def __str__(self):
		return(f"{self.mess_name} {self.mess_menu}")
