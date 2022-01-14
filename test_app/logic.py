import math
import random
from test_app.models import Question, TestedUser, Answer, Answer_variants, Correct_answers, Result


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

    all_questions_list = Question.objects.all()    # all_questions in base
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

    # parsing question_list for test
    test_question_list = []
    for i in range(1, 6):
        test_question_list = test_question_list + question_choose(i, quantity[i-1])

    return test_question_list


# функція перевірки існування користувача в базі та запису його до неї
def check_add_user(data):
    # витягуємо email з запросу
    user_mail = data['email'].strip().lower()
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


# save user answers and get result
def save_answer(data):
    #                data
    # [ {
    #     "user_id": 9,
    #     "question_id": 23,
    #     "answer": ""
    #     "answer_time": [час в секундах]
    # },]


    def get_correct_answers(object):
        model = ['correct_answer1', 'correct_answer2', 'correct_answer3', 'correct_answer4', 'correct_answer5']
        caList = []
        for i in range(0, 5):
            if len(object.serializable_value(model[i])) > 0:
                caList.append(object.serializable_value(model[i]))
        return caList

    # витягуємо користувача через user_id from request after testing
    user = TestedUser.objects.get(id=data[0]['user_id'])
    # змінні що будуть зберігати результат користувача за тест та максимально можливий за цей пул питань
    user_result = 0
    max_test_points = 0

    all_questions_list = Question.objects.all()
    correct_answers = Correct_answers.objects.all()

    for elem in data:
        current_question = all_questions_list.get(id=elem['question_id'])  # вибираєм питання по id from request
        max_test_points += current_question.max_points
        # функція для простого питання
        if current_question.question_type.name == 'S' or current_question.question_type.name == 'SC':
            # якщо відповідь користувача співпадає з записом в полі питання 'correct_answer'
            current_correct_answers = correct_answers.get(id=current_question.correct_answers.id)
            current_correct_answer = current_correct_answers.correct_answer1
            if elem['answer'].strip() == current_correct_answer.strip():
                point = current_question.max_points
            else:
                point = 0
            print(point)
        # функція для simple-choise питання
        # elif current_question.question_type.name == 'SC':
        #     current_answer_variants = answer_variants.get(id=current_question.answer_variants.id)
        #     # current_answer_variants = current_question.answer_variants
        #     print(current_answer_variants)
        #     print(current_answer_variants.numbers_true)
        #     correct_answer = 'variant' + current_answer_variants.numbers_true.strip()
        #     # correct_answer = CORRECT_ANSWERS.correct_answer1
        #     if elem['answer'] == current_answer_variants.serializable_value(correct_answer):
        #         point = current_question.max_points
        #     else:
        #         point = 0
        # функція для multiple-choise питання
        elif current_question.question_type.name == 'MC':
            current_correct_answers = correct_answers.get(id=current_question.correct_answers.id)
            current_correct_answers_list = get_correct_answers(current_correct_answers)
            user_answers = []
            for prop in elem['answer']:
                user_answers.append(elem['answer'][prop])
            print(user_answers)
            print(current_correct_answers_list)
            current_correct_answers_list.sort()
            user_answers.sort()
            if user_answers == current_correct_answers_list:
                point = current_question.max_points
            else:
                point = 0

        # функція для grids питання
        else:
            point = 0
            pass

        user_result += point
        table_entry = Answer(user_id=user, question_id=current_question, answer=user_answers, answer_time=elem['answer_time'], point=point)
        table_entry.save()

    print('max_test_points =', max_test_points)
    print('user_result =', user_result)
    persent = int ((user_result * 100 / max_test_points) * 100) / 100
    print('procent', persent)

    result = Result(user_id=user, points=user_result, persent=persent)
    result.save()
    result_dict = {'user_id': data[0]['user_id'], 'test': '', 'points': user_result, 'persent': persent}

    return result_dict


def save_result(data):
    pass