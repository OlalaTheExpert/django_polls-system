from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

class Category(models.Model):
    category_text = models.CharField(max_length=200)
    
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_text
        
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.name + ' ' + self.email