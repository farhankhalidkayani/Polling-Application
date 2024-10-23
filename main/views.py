from django.shortcuts import render, redirect, get_object_or_404
from main import models
from django.contrib.auth.decorators import login_required
from main.forms import OptionForm, QuestionForm


# Create your views here.
def index(request):
    questions = models.Question.objects.all()
    return render(request, "main/index.html", {"questions": questions})


@login_required
def detail(request, id):
    question = models.Question.objects.get(id=id)
    if request.method == "POST":
        option = request.POST.get("option")
        option = models.Option.objects.get(id=option)
        option.votes += 1
        option.save()
        return redirect("main:result", id=id)

    return render(request, "main/detail.html", {"question": question})


@login_required
def result(request, id):
    question = models.Question.objects.get(id=id)
    return render(request, "main/result.html", {"question": question})


@login_required
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect("main:addoption", id=question.id)
    else:
        form = QuestionForm()
    return render(request, "main/addquestion.html", {"form": form})


# Update Question View (FBV)
@login_required
def update_question(request, id):
    question = get_object_or_404(models.Question, id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("main:index")
    else:
        form = QuestionForm(instance=question)
    return render(request, "main/addquestion.html", {"form": form})


# Delete Question View (FBV)
@login_required
def delete_question(request, pk):
    question = get_object_or_404(models.Question, id=pk)
    if request.method == "POST":
        question.delete()
        return redirect("main:index")
    return render(request, "main/confirmDeletion.html", {"question": question})


# Add Option View (FBV)
@login_required
def add_option(request, id):
    question = get_object_or_404(models.Question, id=id)
    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question = question
            option.save()
            return redirect("main:addoption", id=question.id)
    else:
        form = OptionForm()
    return render(request, "main/addoption.html", {"form": form, "question": question})
