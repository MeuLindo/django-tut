from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
        }),
    ]

admin.site.register(Question, QuestionAdmin)
