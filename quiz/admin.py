from django.contrib import admin
from .models import Question, Answer, Quiz

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_option')
    fields = ('text', 'option1', 'option2', 'option3', 'option4', 'correct_option')

admin.site.register(Question, QuestionAdmin)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'user_answer')
    search_fields = ('user_answer',)
    list_filter = ('question', 'user')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by')
    search_fields = ('title', 'description')
    list_filter = ('created_by',)
