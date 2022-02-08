from django.contrib import admin
from test_app.models import *

from django.contrib.auth.models import Group
admin.site.unregister(Group)

# exported module
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
# exported module


# --------------- CorrectAnswers section for Correct_answers Model-----------------------------------
# old variant
# class CorrectAnswers(admin.ModelAdmin):

class CorrectAnswersResource(resources.ModelResource):

    class Meta:
        model = Correct_answers


class CorrectAnswers(ImportExportActionModelAdmin):
    resource_class = CorrectAnswersResource
    list_display = ('id',
                    'que_id',
                    'correct_answer1',
                    'correct_answer2',
                    'correct_answer3',
                    'correct_answer4',
                    'correct_answer5')
    search_fields = ('correct_answer1', 'correct_answer2', 'correct_answer3', 'correct_answer4', 'correct_answer5')

    def que_id(self, obj):
        result = Question.objects.get(correct_answers=obj)
        return result.id

    que_id.short_description = "id Пит."


admin.site.register(Correct_answers, CorrectAnswers)
# --------------- CorrectAnswers section END---------------------------------------------------------


# --------------- AnswerVariants section for Answer_variants Model-----------------------------------
# old variant
# class AnswerVariants(admin.ModelAdmin):
class AnswerVariantsResource(resources.ModelResource):
    variant1 = fields.Field(column_name='variant1', attribute='variant1', saves_null_values=False)
    variant2 = fields.Field(column_name='variant2', attribute='variant2', saves_null_values=False)
    variant3 = fields.Field(column_name='variant3', attribute='variant3', saves_null_values=False)
    variant4 = fields.Field(column_name='variant4', attribute='variant4', saves_null_values=False)
    variant5 = fields.Field(column_name='variant5', attribute='variant5', saves_null_values=False)
    variant6 = fields.Field(column_name='variant6', attribute='variant6', saves_null_values=False)

    class Meta:
        model = Answer_variants


class AnswerVariants(ImportExportActionModelAdmin):
    resource_class = AnswerVariantsResource
    list_display = ('que_id', 'variant1', 'variant2', 'variant3', 'variant4', 'variant5', 'variant6')
    search_fields = ('variant1', 'variant2', 'variant3', 'variant4', 'variant5', 'variant6')

    def que_id(self, obj):
        result = Question.objects.get(answer_variants=obj)
        return result.id

    que_id.short_description = "Пит. id"


admin.site.register(Answer_variants, AnswerVariants)
# --------------- AnswerVariants section END---------------------------------------------------------


# --------------- Results section for Result Model---------------------------------------------------
# old variant
# class Results(admin.ModelAdmin):

class ResultResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    user_id = fields.Field(column_name='user_id', attribute='user_id', widget=ForeignKeyWidget(TestedUser, 'id'))
    name = fields.Field(column_name='Name', attribute='user_id', widget=ForeignKeyWidget(TestedUser, 'first_name'))
    last_name = fields.Field(column_name='Last name',
                             attribute='user_id',
                             widget=ForeignKeyWidget(TestedUser, 'last_name'))
    email = fields.Field(column_name='email', attribute='user_id', widget=ForeignKeyWidget(TestedUser, 'email'))
    test = fields.Field(column_name='Тест', attribute='test', widget=ForeignKeyWidget(Test, 'name'))

    class Meta:
        model = Result


class Results(ExportActionMixin, admin.ModelAdmin):
    resource_class = ResultResource
    list_display = ('user_id', 'user_lastname_show', 'test', 'points', 'percent')
    search_fields = ('user_id__email',)

    def user_lastname_show(self, obj):
        result = obj.user_id
        return result.last_name

    user_lastname_show.short_description = "User"


admin.site.register(Result, Results)
# --------------- Results section END---------------------------------------------------------


# --------------- Question section for Question Model-------------------------------------------------------------
class QuestionResource(resources.ModelResource):
    id = fields.Field(column_name='id', attribute='id')
    test = fields.Field(column_name='Тест',
                        attribute='test',
                        widget=ForeignKeyWidget(Test, 'name'),
                        saves_null_values=False)
    question_type = fields.Field(column_name='Тип питання',
                                 attribute='question_type',
                                 widget=ForeignKeyWidget(QuestionType, 'name'))
    question_text = fields.Field(column_name='Питання', attribute='question_text')
    max_points = fields.Field(column_name='Бал складності', attribute='max_points')
    # correct_answers = fields.Field(column_name='1', attribute='correct_answers', widget=ForeignKeyWidget(Correct_answers, 'correct_answer1'))
    # correct_answers2 = fields.Field(column_name='2', attribute='correct_answers', widget=ForeignKeyWidget(Correct_answers, 'correct_answer2'))
    # correct_answers3 = fields.Field(column_name='3', attribute='correct_answers', widget=ForeignKeyWidget(Correct_answers, 'correct_answer3'))
    # correct_answers4 = fields.Field(column_name='4', attribute='correct_answers', widget=ForeignKeyWidget(Correct_answers, 'correct_answer4'))
    # correct_answers5 = fields.Field(column_name="5", attribute='correct_answers', widget=ForeignKeyWidget(Correct_answers, 'correct_answer5'))
    # answer_variants1 = fields.Field(column_name='Варіант відповіді 1', attribute='answer_variants', widget=ForeignKeyWidget(Answer_variants, 'variant1'))
    # answer_variants2 = fields.Field(column_name='Варіант відповіді 2', attribute='answer_variants', widget=ForeignKeyWidget(Answer_variants, 'variant2'))
    # answer_variants3 = fields.Field(column_name='Варіант відповіді 3', attribute='answer_variants', widget=ForeignKeyWidget(Answer_variants, 'variant3'))
    # answer_variants4 = fields.Field(column_name='Варіант відповіді 4', attribute='answer_variants', widget=ForeignKeyWidget(Answer_variants, 'variant4'))
    # answer_variants5 = fields.Field(column_name='Варіант відповіді 5', attribute='answer_variants', widget=ForeignKeyWidget(Answer_variants, 'variant5'))
    # answer_variants6 = fields.Field(column_name='Варіант відповіді 6', attribute='answer_variants', widget=ForeignKeyWidget(Answer_variants, 'variant6'))

    class Meta:
        model = Question
        exclude = ['question_image']


class Questions(ImportExportActionModelAdmin):
    resource_class = QuestionResource
    list_display = ('pk', 'test', 'question_type', 'question_text', 'max_points', 'answer_variants', 'correct_answers')
    list_display_links = ('question_text', 'test', 'max_points', 'answer_variants', 'correct_answers')
    search_fields = ('question_text', )
    list_filter = ("test", 'question_type', 'max_points')


admin.site.register(Question, Questions)


# --------------- Tests section for Test Model-----------------------------------------------------
class Tests(admin.ModelAdmin):
    list_display = ('name', 'quantity_questions', 'time_for_test', 'is_active')
    list_display_links = ('name',)


admin.site.register(Test, Tests)
# --------------- Tests section END ---------------------------------------------------------------


# --------------- Tested user and  Answers sections for TestedUser Model, Answer Model-------------
class Testeduser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(TestedUser, Testeduser)


class Answers(admin.ModelAdmin):
    list_display = ('user_id', 'answer', 'answer_time', 'point', 'question_id')


admin.site.register(Answer, Answers)
# --------------- Tested user and  Answers sections END---------------------------------


#  Для показу та додавання питань іншого типу в адмінці
# ======================================================
# class Question_t(admin.ModelAdmin):
#     list_display = ('name',)


# admin.site.register(QuestionType, Question_t)
# ======================================================
