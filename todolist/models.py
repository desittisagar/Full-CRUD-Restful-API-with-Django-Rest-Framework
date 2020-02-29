from django.db import models

# Create your models here.

class rest_api_model(models.Model):
	desc = models.CharField(max_length = 100)