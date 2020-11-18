from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    # extra = 3 # По умолчанию покажет доп количство полей


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)


# Отбеляет блоки для большой формы
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)

# простое добавление модели
# admin.site.register(Question)

# меняем поля местами в админке
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
#
# admin.site.register(Question, QuestionAdmin)