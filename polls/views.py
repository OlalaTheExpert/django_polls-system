from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Category

# Create your views here.
def polls_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/polls_list.html', {'questions': questions})

def polls_details(request, question_text):
    question = Question.objects.get(question_text=question_text)
    return render(request, 'polls/polls_details.html', {'question': question})

def polls_results(request, question_text):
    question = Question.objects.get(question_text=question_text)
    return render(request, 'polls/polls_results.html', {'question': question})

def polls_vote(request, question_text):
    question = Question.objects.get(question_text=question_text)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.question_text,)))
