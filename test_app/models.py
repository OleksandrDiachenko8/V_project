from django.db import models


# Модель що описує існуючі тести
class Test(models.Model):
    name = models.CharField('Назва тесту', max_length=50)
    quantity_questions = models.PositiveSmallIntegerField('Кількість питань', help_text='Скільки питань видавати для тесту?')
    time_for_test = models.PositiveSmallIntegerField('Час тесту', default=60, help_text='Час тесту в хвилинах')
    is_active = models.BooleanField()
    description = models.TextField(help_text='Інформація для користувача', blank=True)
    by_text = models.TextField(help_text='Для виводу по закінченню тесту', blank=True)

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return f'{self.name}'


# Модель що описує можливі типи питань (коротка відповідь, одиночний та множинний вибір, вставка пропусків)
class QuestionType(models.Model):
    Short = 'S'
    Single = 'SC'
    Multiple = 'MC'
    Grid = 'G'
    QUESTION_TYPE_CHOICES = [
        (Short, 'Вписати відповідь'),
        (Single, 'Одиночний вибір'),
        (Multiple, 'Множинний вибір'),
        (Grid, 'Grid'),
    ]
    name = models.CharField('Тип питання', max_length=2, choices=QUESTION_TYPE_CHOICES, default=Short, unique=True)
    description = models.TextField('Опис', blank=True)

    class Meta:
        verbose_name = 'Question type'
        verbose_name_plural = 'Question type'

    def __str__(self):
        return self.description


# Модель що описує відповіді на питання
class Answer_variants(models.Model):
    variant1 = models.CharField('Варiант 1', max_length=100, blank=True, help_text='при наявності')
    variant2 = models.CharField('Варiант 2', max_length=100, blank=True, help_text='при наявності')
    variant3 = models.CharField('Варiант 3', max_length=100, blank=True, help_text='при наявності')
    variant4 = models.CharField('Варiант 4', max_length=100, blank=True, help_text='при наявності')
    variant5 = models.CharField('Варiант 5', max_length=100, blank=True, help_text='при наявності')
    variant6 = models.CharField('Варiант 6', max_length=100, blank=True, help_text='при наявності')

    class Meta:
        verbose_name = 'Answer variants'
        verbose_name_plural = 'Answer variants'

    def __str__(self):
        return f'Id {self.id}'


# Модель що описує відповіді на питання
class Correct_answers(models.Model):
    correct_answer1 = models.CharField('Правильна відповідь 1', max_length=100, help_text='Основна відповідь')
    correct_answer2 = models.CharField('Правильна відповідь 2', max_length=100, blank=True, help_text='при наявності', null=True)
    correct_answer3 = models.CharField('Правильна відповідь 3', max_length=100, blank=True, help_text='при наявності', null=True)
    correct_answer4 = models.CharField('Правильна відповідь 4', max_length=100, blank=True, help_text='при наявності', null=True)
    correct_answer5 = models.CharField('Правильна відповідь 5', max_length=100, blank=True, help_text='при наявності', null=True)

    class Meta:
        verbose_name = 'correct answer'
        verbose_name_plural = 'correct answers'

    def __str__(self):
        return f'Id {self.id}. {self.correct_answer1}'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.PROTECT, blank=True)
    question_type = models.ForeignKey(QuestionType, on_delete=models.PROTECT)
    question_text = models.TextField()
    question_image = models.ImageField(upload_to=None, blank=True)
    max_points = models.IntegerField()
    correct_answers = models.OneToOneField(Correct_answers, on_delete=models.PROTECT)
    answer_variants = models.OneToOneField(Answer_variants, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


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

    # return f'Id {self.id}: {self.email}'


class Answer(models.Model):
    user_id = models.ForeignKey(TestedUser, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.TextField(blank=True)
    answer_time = models.IntegerField(blank=True)
    point = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Відповідь користувача'
        verbose_name_plural = 'Відповіді користувачів'


class Result(models.Model):
    user_id = models.ForeignKey(TestedUser, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.PROTECT, blank=True)
    points = models.IntegerField(blank=True)
    percent = models.DecimalField(max_digits=4, decimal_places=1)


    class Meta:
        verbose_name = 'Результат тесту'
        verbose_name_plural = 'Результати тесту'


    def __str__(self):
        return f'{self.user_id} - {self.points}'
