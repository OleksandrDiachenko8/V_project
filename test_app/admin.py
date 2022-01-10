from django.contrib import admin
from test_app.models import *


class Test(admin.ModelAdmin):
    list_display = ('name', 'quantity_questions', 'time_for_test')
    list_display_links = ('quantity_questions', 'time_for_test')


admin.site.register(Tests, Test)


class Question_a(admin.ModelAdmin):
    list_display = ('question_text', 'test', 'max_points', 'correct_answer', 'answer_variants', 'question_type')
    list_display_links = ('question_text', 'test', 'max_points', 'answer_variants')
    search_fields = ('question_text', )


admin.site.register(Question, Question_a)


class Question_t(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(QuestionType, Question_t)


class AnswerVariants(admin.ModelAdmin):
    list_display = ('variant1', 'istrue1', 'variant2', 'istrue2', 'variant3', 'istrue3', 'variant4', 'istrue4', \
    'variant5', 'istrue5', 'variant6', 'istrue6',)
    search_fields = ('variant1', 'variant2', 'variant3', 'variant4', 'variant5', 'variant6',)


admin.site.register(Answer_variants, AnswerVariants)


class Testeduser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(TestedUser, Testeduser)


class Answers(admin.ModelAdmin):
    list_display = ('user_id', 'question_id', 'answer', 'answer_time', 'point')


admin.site.register(Answer, Answers)


# class Result(admin.ModelAdmin):
#     list_display = ('user_id', 'points')
#
#
# admin.site.register(Result, Result)




