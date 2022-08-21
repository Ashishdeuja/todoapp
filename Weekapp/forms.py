from django import forms
from Weekapp.models import Question,Answer
from django import forms
from .models import Todo
  


class QuestionForm(forms.ModelForm):
    its_question = forms.ModelChoiceField(
        queryset=Question.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'placeholder':'Select  Type',
            'class':'form-select'
            }),
            empty_label="Please Select your Question")
        
    # answer = forms.CharField(required=True)

    class Meta:
        model = Answer
        fields = '__all__'


        
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields="__all__"