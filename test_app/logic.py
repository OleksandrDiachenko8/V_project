import math
import random
from test_app.models import Question, TestedUser, Answer, Correct_answers, Result, Test


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
                # if bool(elem.question_image) != 0:
                #     print(elem.question_image.path)
                #     elem.question_image = elem.question_image.path
                q_array.append(elem)
                k += 1
        return q_array

    current_test = Test.objects.filter(is_active=True)[0]

    # all_questions in base
    all_questions_list = Question.objects.all()
    # only_questions in this test
    # all_questions_list = Question.objects.filter(test=current_test)

    questions_quantity = len(all_questions_list)      # всього питань
    test_quantity = current_test.quantity_questions   # питань потрібно для теста

    if test_quantity <= questions_quantity:
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
    else:
        test_question_list = []

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
    #     "answer": {},
    #     "answer_time": [час в секундах]
    # },]
    def get_correct_answers(obj):
        model = ['correct_answer1', 'correct_answer2', 'correct_answer3', 'correct_answer4', 'correct_answer5']
        ca_list = []
        for i in range(0, 5):
            if len(obj.serializable_value(model[i])) > 0:
                ca_list.append(obj.serializable_value(model[i]))
        return ca_list

    # витягуємо користувача через user_id from request after testing
    user = TestedUser.objects.get(id=data[0]['user_id'])
    # змінні що будуть зберігати результат користувача за тест та максимально можливий за цей пул питань
    user_result = 0
    max_test_points = 0

    all_questions_list = Question.objects.all()
    correct_answers = Correct_answers.objects.all()

    for elem in data:
        current_question = all_questions_list.get(id=elem['question_id'])  # вибираєм питання по id_from_request
        max_test_points += current_question.max_points
        # функція для простого питання
        if current_question.question_type.name == 'S' or current_question.question_type.name == 'SC':
            user_answers = [elem['answer']]
            # якщо відповідь користувача співпадає з записом в полі питання 'correct_answer'
            current_correct_answers = correct_answers.get(id=current_question.correct_answers.id)
            current_correct_answer = current_correct_answers.correct_answer1
            if elem['answer'].strip().lower() == current_correct_answer.strip().lower():
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

    percent = int((user_result * 100 / max_test_points) * 100) / 100
    print('max_test_points =', max_test_points)
    print('user_result =', user_result)
    print('percent =', percent)
    curr_test = Test.objects.filter(is_active=True)[0]
    print(curr_test)

    result = Result(user_id=user, points=user_result, percent=percent, test=curr_test)
    result.save()
    result_dict = {'user_id': data[0]['user_id'], 'points': user_result, 'percent': percent}
    return result_dict


def get_test_time():
    current_test = Test.objects.filter(is_active=True)[0]
    current_test_time = current_test.time_for_test
    return current_test_time
