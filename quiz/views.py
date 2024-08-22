from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout

@login_required
def take_quiz(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        score = 0
        total = questions.count()
        errors = []

        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option is None:
                errors.append(f'You missed question {question.id}. Please select an answer.')
            elif selected_option == question.correct_option:
                score += 1

        if errors:
            return render(request, 'quiz/take_quiz.html', {
                'questions': questions,
                'errors': errors,
            })

        return render(request, 'quiz/result.html', {
            'score': score,
            'total': total,
        })

    return render(request, 'quiz/take_quiz.html', {
        'questions': questions,
    })
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect view
    else:
        form = UserCreationForm()

    return render(request, 'quiz/register.html', {'form': form})

def home(request):
    return render(request, 'quiz/home.html')

@login_required
def profile(request):
    return render(request, 'quiz/profile.html')

@login_required
def logged_out_view(request):
    return render(request, 'registration/logged_out.html')

