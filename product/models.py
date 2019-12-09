from django.db import models

class Sale(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	sale = models.IntegerField()

	def __str__(self):
		return '{} => {}'.format(self.title, self.sale)


class Good(models.Model):
	title = models.CharField(max_length=128)
	description = models.TextField()
	price = models.IntegerField()
	sale1 = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title


