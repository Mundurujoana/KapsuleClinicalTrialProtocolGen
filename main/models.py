from django.db import models

# Create your models here.

# Question Model
class Question(models.Model):
  title=models.CharField(max_length=250)
  details=models.TextField()
  time=models.DateTimeField(auto_now_add=True)
  
#   define a method if we access this question in the admin what should it return
  def _str_(self):
     return self.title

# Answer Model
class Answer(models.Model):
  question=models.ForeignKey(Question,on_delete=models.CASCADE)
  details=models.TextField()
  time=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.details
