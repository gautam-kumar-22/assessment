from django.contrib import admin
from .models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'relevance_marks']


admin.site.register(Question, QuestionAdmin)
