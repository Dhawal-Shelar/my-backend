from django.db import models




class FeedbackModel(models.Model):
  email = models.EmailField()
  name = models.CharField(max_length=255)
  feedback = models.TextField()
  

# Create your models here.
