import random

symbols = {
	2 : {
		0 : "0",
		1 : "1"
	},
	8 : {
		0 : "0",
		1 : "1",
		2 : "2",
		3 : "3",
		4 : "4",
		5 : "5",
		6 : "6",
		7 : "7"
	},
	10 : {
		0 : "0",
		1 : "1",
		2 : "2",
		3 : "3",
		4 : "4",
		5 : "5",
		6 : "6",
		7 : "7",
		8 : "6",
		9 : "9"
	},
	16 : {
		0 : "0",
		1 : "1",
		2 : "2",
		3 : "3",
		4 : "4",
		5 : "5",
		6 : "6",
		7 : "7",
		8 : "6",
		9 : "9",
		10 : "A",
		11 : "B",
		12 : "C",
		13 : "D",
		14 : "E",
		15 : "F"
	}
}

system_name = {
	2 : "Bin",
	8 : "Oct",
	10 : "Dec",
	16 : "Hex"
}

def keepDecimal(value: float) -> float:
	return value - int(value)

def convertSys(value: float, base: int, precision: int) -> str:
	whole: str = ""
	fractional: str = ""

	val = int(value)
	while (val > 0):
		whole = symbols[base][val % base] + whole
		val = val // base

	val = keepDecimal(value)
	i = 0
	while (i < precision):
		val = base * keepDecimal(val)
		fractional += symbols[base][int(val)]
		i += 1

	if fractional == "":
		return whole
	return whole + "." + fractional

while True:
	random_float = random.uniform(0, 100)
	precision = random.randint(0, 5)
	number_systems = random.sample([2, 8, 10, 16], 2)
	system_names = [system_name[number_systems[0]], system_name[number_systems[1]]]

	converted = convertSys(random_float, number_systems[0], precision+2)
	answer = convertSys(random_float, number_systems[1], precision)

	# print(f"Random Float: {random_float}")
	print(f"Precision: {precision}")
	print(f"Convert {system_names[0]} {converted} to {system_names[1]}")

	toCheck = input("Enter your answer: ")

	if (answer == toCheck):
		print("Yes, your answer is correct")
	else:
		print(f"Incorrect answer. The correct answer was {answer}")

	input()