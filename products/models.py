from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
	title=models.CharField(max_length=200)
	pubdate=models.DateTimeField()
	body=models.TextField()
	url=models.TextField()
	image=models.ImageField(upload_to='images/')
	icon=models.ImageField(upload_to='images/')
	votes_total=models.IntegerField(default=1)
	hunter=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title
 
	def summary(self):
		return self.body[:100]

	def pubdate_pretty(self):
		return self.pubdate.strftime('%b %e %Y')
	
