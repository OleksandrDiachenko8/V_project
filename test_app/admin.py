from django.contrib import admin
from test_app.models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class Questions(admin.ModelAdmin):
    list_display = ('pk', 'test', 'question_type', 'question_text', 'max_points', 'answer_variants', 'correct_answers')
    list_display_links = ('question_text', 'test', 'max_points', 'answer_variants', 'correct_answers')
    search_fields = ('question_text', )
    list_filter = ("test", 'question_type', 'max_points')


admin.site.register(Question, Questions)


class Tests(admin.ModelAdmin):
    list_display = ('name', 'quantity_questions', 'time_for_test', 'is_active')
    list_display_links = ('name',)


admin.site.register(Test, Tests)


#  Для показу та додавання питань іншого типу в адмінці
# ======================================================
# class Question_t(admin.ModelAdmin):
#     list_display = ('name',)


# admin.site.register(QuestionType, Question_t)
# ======================================================

class AnswerVariants(admin.ModelAdmin):
    list_display = ('que_id', 'variant1', 'variant2', 'variant3', 'variant4', 'variant5', 'variant6',)
    search_fields = ('variant1', 'variant2', 'variant3', 'variant4', 'variant5', 'variant6')

    def que_id(self, obj):
        result = Question.objects.get(answer_variants=obj)
        return result.id

    que_id.short_description = "Пит. id"


admin.site.register(Answer_variants, AnswerVariants)


class CorrectAnswers(admin.ModelAdmin):
    list_display = ('que_id', 'id', 'correct_answer1', 'correct_answer2', 'correct_answer3', 'correct_answer4', 'correct_answer5')
    search_fields = ('correct_answer1', 'correct_answer2', 'correct_answer3', 'correct_answer4', 'correct_answer5')

    def que_id(self, obj):
        result = Question.objects.get(correct_answers=obj)
        return result.id

    que_id.short_description = "Пит. id"


admin.site.register(Correct_answers, CorrectAnswers)


class Testeduser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(TestedUser, Testeduser)


class Answers(admin.ModelAdmin):
    list_display = ('user_id', 'answer', 'answer_time', 'point', 'question_id')


admin.site.register(Answer, Answers)


class Results(admin.ModelAdmin):
    list_display = ('user_id', 'test', 'points', 'percent')


admin.site.register(Result, Results)
