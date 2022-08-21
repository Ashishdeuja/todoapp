from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from Weekapp.models import Question, Answer
from .forms import QuestionForm
from .forms import TodoForm
from .models import Todo
  
# from django.shortcuts import HttpResponse 

# Create your views here.

def index(request):
    # text = "<h1><li>Welcome to my app !</li></h1"
    # return HttpResponse(text)
    # # return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
    lists =[1,2,3,4,5]
    context = {"name":"Ashish","rollno":"04","lists":lists}
    return render(request, "index.html", context)

def page1(request):
    return render(request, "page1.html") 

def question(request):
    questions=Question.objects.all()
    context={"questions":questions}
    return render(request, "questions.html", context)

# def answer(request):
#     answers=Answer.objects.all()
#     context={"answers":answers}
#     return render (request,"questions.html", context)


def question_form(request):
    # if request.method == "POST":
    #     form_question = request.POST.get("selected_question")
    #     question = Question.objects.filter(question=form_question)[0]
    #     form_answer = request.POST.get("answer")
    #     ans_with_question = Answer(its_question=question, answer =form_answer)
    #     ans_with_question.save()
    #     messages.info(request,'You have successfully added a data to Answer table')
    #     return redirect('/question')
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            messages.warning(request, 'You Have Successfully added a data to Answer table')
            return redirect('/question')
    else:
        # questions=Question.objects.all()
        # context= {"questions":questions}
        # return render(request,"form.html", context)
        form = QuestionForm()
        context={"form":form}
        return render(request,"django_form.html",context)

def todo(request):
  
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TodoForm()
  
    page = {
             "forms" : form,
             "list" : item_list,
             "title" : "Note",
           }
    return render(request, 'todo.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Data removed successfully !!!")
    return redirect('/')