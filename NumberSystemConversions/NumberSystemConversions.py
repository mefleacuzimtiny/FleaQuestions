import random
from math import log, ceil

symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '6', '9', 'A', 'B', 'C', 'D', 'E', 'F']

system_name = {
	2 : "Bin",
	8 : "Oct",
	10 : "Dec",
	16 : "Hex"
}

def keepDecimal(value: float) -> float:
	return value - int(value)

def convertSys(value: float, base: int, prec_ans: int) -> str:
	whole: str = ""
	fractional: str = ""

	val = int(value)
	while (val > 0):
		whole = symbols[val % base] + whole
		val = val // base

	val = keepDecimal(value)
	for i in range(prec_ans):
		val = base * keepDecimal(val)
		fractional += symbols[int(val)]

	if fractional == "":
		return whole
	return whole + "." + fractional

while True:
	random_float = random.uniform(0, 100)
	bases = random.sample([2, 8, 10, 16], 2)
	system_names = [system_name[bases[0]], system_name[bases[1]]]
	prec_ans = random.randint(0, 8)
	prec_ques = int(ceil(prec_ans * log(bases[1]) / log(bases[0])))

	converted = convertSys(random_float, bases[0], prec_ques)
	answer = convertSys(random_float, bases[1], prec_ans)

	# print(f"Random Float: {random_float}")
	print(f"Precision: {prec_ans}")
	print(f"Convert {system_names[0]} {converted} to {system_names[1]}")

	toCheck = input("Enter your answer: ")

	if (answer == toCheck):
		print("Yes, your answer is correct")
	else:
		print(f"Incorrect answer. The correct answer was {answer}")

	input()