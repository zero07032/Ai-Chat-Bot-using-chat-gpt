from django.shortcuts import render

from .question_response import answer


def home(request):
    context = {}
    return render(request, "home.html", context)


def get_answer(request):
    question = request.POST.get("question")
    question_answer = "No result found"
    if question:
        question_answer = answer(question)
    context = {"question_answer": question_answer}
    return render(request, "home.html", context)
