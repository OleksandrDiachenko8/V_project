from django.db import models


# Модель що описує можливі типи питань (коротка відповідь, одиночний та множинний вибір, вставка пропусків)
class QuestionType(models.Model):
    Short = 'S'
    Single = 'SC'
    Multiple = 'MC'
    Grid = 'G'
    QUESTION_TYPE_CHOICES = [
        (Short, 'Коротка відповідь'),
        (Single, 'Одиночний вибір'),
        (Multiple, 'Множинний вибір'),
        (Grid, 'Insert_blanks'),
    ]
    name = models.CharField('Тип питання', max_length=2, choices=QUESTION_TYPE_CHOICES, default=Short)
    description = models.TextField('Опис', blank=True)

    class Meta:
        verbose_name = 'Тип питання'
        verbose_name_plural = 'Типи питань'

    def __str__(self):
        return self.name


# Модель що описує існуючі тести
class Tests(models.Model):
    name = models.CharField('Назва тесту', max_length=20)
    quantity_questions = models.IntegerField('Кількість питань в тесті')
    time_for_test = models.PositiveSmallIntegerField('Час тесту в хвилинах', default=60)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тести'

    def __str__(self):
        return f'Id {self.id}: {self.name}'


# Модель що описує відповіді на питання
class Answer_variants(models.Model):
    variant1 = models.CharField('Варiант 1', max_length=100, blank=True)
    istrue1 = models.BooleanField('вірний?', default=False)
    variant2 = models.CharField('Варiант 2', max_length=100, blank=True)
    istrue2 = models.BooleanField('вірний?', default=False)
    variant3 = models.CharField('Варiант 3', max_length=100, blank=True)
    istrue3 = models.BooleanField('вірний?', default=False)
    variant4 = models.CharField('Варiант 4', max_length=100, blank=True)
    istrue4 = models.BooleanField('вірний?', default=False)
    variant5 = models.CharField('Варiант 5', max_length=100, blank=True)
    istrue5 = models.BooleanField('вірний?', default=False)
    variant6 = models.CharField('Варiант 6', max_length=100, blank=True)
    istrue6 = models.BooleanField('вірний?', default=False)

    class Meta:
        verbose_name = 'Варiанти відповіді'
        verbose_name_plural = 'Варiанти відповіді'

    def __str__(self):
        return f'Id {self.id}'


class Question(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.SET_NULL, null=True, blank=True)
    question_type = models.ForeignKey(QuestionType, on_delete=models.SET_NULL, null=True)
    question_text = models.TextField()
    question_image = models.ImageField(upload_to=None, blank=True)
    max_points = models.IntegerField()
    correct_answer = models.CharField(max_length=100, default='answer')
    answer_variants = models.OneToOneField(Answer_variants, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Питання'
        verbose_name_plural = 'Питання'

    def __str__(self):
        return f'Id {self.id}: {self.question_text}'


class TestedUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'Користувач тесту'
        verbose_name_plural = 'Користувачі тесту'

    def __str__(self):
        return f'Id {self.id}: {self.email}'


class Answer(models.Model):
    user_id = models.ForeignKey(TestedUser, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.CharField(max_length=40, blank=True)
    answer_time = models.IntegerField(blank=True, default=0)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Відповідь користувача'
        verbose_name_plural = 'Відповіді користувача'


class Result(models.Model):
    user_id = models.ForeignKey(TestedUser, on_delete=models.CASCADE)
    test = models.ForeignKey(Tests, on_delete=models.SET_NULL, blank=True, null=True)
    points = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Результат тесту'
        verbose_name_plural = 'Результати тесту'

    def __str__(self):
        return f'{self.user_id}-{self.points}'



#
# class GridAnswer(models.Model):
#     question_id = models.OneToOneField(Question, on_delete=models.CASCADE, null=True)
#     correct_answer = models.CharField('', max_length=40, blank=True)
#     answer_line = models.CharField('', max_length=30)
#     answer_column = models.CharField('', max_length=30)
#
#     class Meta:
#         verbose_name = 'Відповідь на вставку пропусків'
#         verbose_name_plural = 'Відповіді на вставку пропусків'
