def get_answer(question, answers):
	if question in answers:
		return answers[question]
	else:
		return 'Неправильно!'


answers = {
		"привет": "И тебе привет!",
		"как дела": "Лучше всех",
		"пока": "Увидимся"
		}
question = input('Введите слово: ').lower()


print(get_answer(question, answers))