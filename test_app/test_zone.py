import openpyxl

book = openpyxl.Workbook()
sheet = book.active

sheet["A2"] = 56
sheet["A5"] = "Hello"

book.save("filetest.xlsx")
book.close()

[
    {
        "user_id": 13,
        "time_for_test": 60,
        "test_description": "Це вступний тест, намагайтеся відповідати вірно",
        "test_by": "Це кінець"
    },
    {
        "id": 5,
        "question_type": 1,
        "question_text": "JS. Напишіть результат виконання: let y = 2 - \"2\" – 2",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 6,
        "question_type": 1,
        "question_text": "Яка властивість CSS визначає розмір тексту?",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 16,
        "question_type": 3,
        "question_text": "Які теги html існують",
        "question_image": null,
        "answer_variants": {
            "variant1": "<b>",
            "variant2": "<css>",
            "variant3": "<em>",
            "variant4": "<h6>",
            "variant5": "<href>"
        }
    },
    {
        "id": 15,
        "question_type": 2,
        "question_text": "Як вставити картинку в HTML?",
        "question_image": null,
        "answer_variants": {
            "variant1": "<img src=\"http://site.com/image.jpg\">",
            "variant2": "<image>http://site.com/image.jpg</image>",
            "variant3": "<img>http://site.com/image.jpg</img>",
            "variant4": "<image source=\"http://site.com/image.jpg\">",
            "variant5": "img=image.jpg"
        }
    },
    {
        "id": 18,
        "question_type": 3,
        "question_text": "Довільне питання з багатьма варіантами номер 8",
        "question_image": null,
        "answer_variants": {
            "variant1": "Варіант 1",
            "variant2": "Варіант 2",
            "variant3": "Варіант 3",
            "variant4": "Варіант 4",
            "variant5": "Варіант 5"
        }
    },
    {
        "id": 22,
        "question_type": 3,
        "question_text": "БУМЕРангБУМЕРангБУМЕРангБУМЕРангБУМЕРанг",
        "question_image": null,
        "answer_variants": {
            "variant1": "БУМЕРанг",
            "variant2": "БУМЕРанг",
            "variant3": "БУМЕРанг",
            "variant4": "БУМЕРанг",
            "variant5": "БУМЕРанг",
            "variant6": "БУМЕРанг"
        }
    },
    {
        "id": 7,
        "question_type": 1,
        "question_text": "Мінімальна одиниця кількості інформації називається",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 4,
        "question_type": 1,
        "question_text": "Визначте правило, використане при обробці інформації, та закінчіть послідовність:  \r\nВОРОГ – 2, СВІТ – 0, КОЛОБОК – 3, НОРМА – 1, ОБОРОНОЗДАТНІСТЬ – 4, АЛГОРИТМ – …",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 14,
        "question_type": 2,
        "question_text": "Яке число потрібно поставити замість знака питання?",
        "question_image": null,
        "answer_variants": {
            "variant1": "17",
            "variant2": "18",
            "variant3": "19",
            "variant4": "20",
            "variant5": "21",
            "variant6": "22"
        }
    },
    {
        "id": 20,
        "question_type": 1,
        "question_text": "question_text2",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 12,
        "question_type": 2,
        "question_text": "Яку фігуру можно зібрати?",
        "question_image": "/media/None/3.jpg",
        "answer_variants": {
            "variant1": "1",
            "variant2": "2",
            "variant3": "3",
            "variant4": "4",
            "variant5": "5"
        }
    },
    {
        "id": 13,
        "question_type": 2,
        "question_text": "Бізнесмен купив кілька самокатів за 2500 $, а продав їх за 4500 $, заробивши за кожен самокат 100 $. Скільки самокатів він продав?",
        "question_image": null,
        "answer_variants": {
            "variant1": "45",
            "variant2": "30",
            "variant3": "25",
            "variant4": "20",
            "variant5": "10"
        }
    },
    {
        "id": 8,
        "question_type": 1,
        "question_text": "Тип числа с десятковою крапкою в python",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 17,
        "question_type": 3,
        "question_text": "До оптоволоконного кабелю відносяться такі характеристики:",
        "question_image": null,
        "answer_variants": {
            "variant1": "можливість використання кабелю на великих відстанях без регенерації сигналу",
            "variant2": "низька вартість кабелю",
            "variant3": "відсутність чутливості до електромагнітних перешкод",
            "variant4": "чутливість до електромагнітних перешкод",
            "variant5": "-  кабель не можна розкрити та перехопити дані"
        }
    },
    {
        "id": 3,
        "question_type": 1,
        "question_text": "Число 15 десяткової системи числення має запис у двійковій системі:",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 2,
        "question_type": 1,
        "question_text": "Що буде виведено в консоль?",
        "question_image": "/media/None/1.jpg",
        "answer_variants": null
    },
    {
        "id": 9,
        "question_type": 1,
        "question_text": "Функція що повертає довжину об’єкта в python",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 1,
        "question_type": 1,
        "question_text": "Якщо 5% від числа дорівнюють 2, то 100% дорівнюють:",
        "question_image": null,
        "answer_variants": null
    },
    {
        "id": 11,
        "question_type": 2,
        "question_text": "Коли зламався комп'ютер, його господар сказав: «Пам'ять не могла вийти з ладу». Його син припустив, що згорів процесор а вінчестер справний. Майстер із ремонту сказав, що з процесором все гаразд, а пам'ять несправна. В результаті виявилося, що двоє з них сказали все правильно, а третій – все неправильно. Що ж вийшло з ладу?",
        "question_image": null,
        "answer_variants": {
            "variant1": "Пам'ять",
            "variant2": "Процесор",
            "variant3": "Вінчестер",
            "variant4": "Все одразу"
        }
    },
    {
        "id": 19,
        "question_type": 1,
        "question_text": "question_text",
        "question_image": null,
        "answer_variants": null
    }
]