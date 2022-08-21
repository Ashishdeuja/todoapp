
from django.contrib import admin

# Register your models here.
from Weekapp.models import Question, Answer
from .models import Todo

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Todo)
