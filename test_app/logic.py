import math
import random
from test_app.models import Question, TestedUser


# функція вибірки питань
def question():
    def question_choose(difficulty, quantity):
        k = 0
        q_array = []
        while k < quantity:
            a = random.randrange(0, len(all_questions_list.filter(max_points=difficulty)))
            elem = all_questions_list.filter(max_points=difficulty)[a]
            if elem in q_array:
                pass
            else:
                q_array.append(elem)
                k += 1
        return q_array

    all_questions_list = Question.objects.all()
    questions_quantity = len(all_questions_list)   # всього питань
    test_quantity = 10                             # питань потрібно для теста
    # Визначення скільки питань кожного виду для тесту, поміняти як визначиться звідки брати дані
    five_quantity = math.ceil(len(all_questions_list.filter(max_points=5)) * test_quantity / questions_quantity)
    four_quantity = round(len(all_questions_list.filter(max_points=4)) * test_quantity / questions_quantity)
    three_quantity = round(len(all_questions_list.filter(max_points=3)) * test_quantity / questions_quantity)
    two_quantity = round(len(all_questions_list.filter(max_points=2)) * test_quantity / questions_quantity)
    one_quantity = test_quantity - five_quantity - four_quantity - three_quantity - two_quantity

    # quantity - кількість питань кожного рівня
    quantity = [one_quantity, two_quantity, three_quantity, four_quantity, five_quantity]
    # print(quantity) - видалити потім

    test_question_list = []
    for i in range(1, 6):
        test_question_list = test_question_list + question_choose(i, quantity[i-1])

    print(test_question_list)
    return test_question_list


# функція перевірки існування користувача в базі та запису його до неї
def check_add_user(data):
    # витягуємо email з запросу
    user_mail = data['email']
    # шукаємо в базі юзера з таким email
    users_check = TestedUser.objects.all().filter(email=user_mail)
    if len(users_check) > 0:
        print('user already exists!!')
        return users_check[0].id
    else:
        # додаємо в базу
        user = TestedUser(first_name=data['first_name'], last_name=data['last_name'], email=user_mail)
        user.save()
        return user.id


def result_fit(data):
    answer_block = data.objects.all()
    print(answer_block)
