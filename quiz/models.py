from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    
    CORRECT_OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    
    correct_option = models.CharField(
        max_length=7,
        choices=CORRECT_OPTION_CHOICES,
        verbose_name="Correct Option"
    )

    def __str__(self):
        return self.text

   

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    user_answer = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.question.text} - {self.user_answer}'




class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes_created')
    questions = models.ManyToManyField(Question, related_name='quizzes')

    def __str__(self):
        return self.title
