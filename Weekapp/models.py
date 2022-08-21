from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=40)
    

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.question

class Answer(models.Model):
    
    its_question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    answer=RichTextField()
    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.answer

class Todo(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)
  
    def __str__(self):
        return self.title