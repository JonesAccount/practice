from random import *

languages = ("python", "java", "c#", "javascript")
foods = ("пельмени", "хлеб с маслом", "мясо", "мамин борщ")
loves = ["никому", "Мегану Фоксу", "Райану Гослингу", "персонажу из игры", "Куплинову"]

shuffle(loves)
randomaizer_ran = random()
num_gender = round(randomaizer_ran)
randomaizer_uni = uniform(0, 3)
num_uni = round(randomaizer_uni)

favorate_food = choice(foods)
favorate_lan = languages[num_uni]
age = randint(15, 40)
gender = None

if num_gender == 1:
    gender = "мужской"
else:
    gender = "женский"
    
information_about_jaba = lambda: "🐸ИНФОРМАЦИЯ О ЖАБЕ\n" + "- Возраст: " + str(age) + "\n- Пол: " + gender + "\n- Любимый язык: " + favorate_lan + "\n- Любимая еда: " + favorate_food + "\n- Кому влюблен: " + loves[0]

print(information_about_jaba())
