#include <iostream>
#include <map>
#include <random>
#include <unordered_set>
#include <cmath>

std::string lineIn(std::string prompt, bool ignore_empty = true) {
	std::string toReturn = "";
	if (ignore_empty) {
		while (toReturn == "") {
			std::cout << prompt;
			std::getline(std::cin, toReturn);
		}
	} else {
		std::cout << prompt;
		std::getline(std::cin, toReturn);
	}
	return toReturn;
}

std::random_device dev;
std::mt19937 rng(dev());

std::map<int, std::string> NumSysNames {
	{2, "Bin"},
	{8, "Oct"},
	{10, "Dec"},
	{16, "Hex"}
};

std::map<int, std::string> symbols {
	{0, "0"},
	{1, "1"},
	{2, "2"},
	{3, "3"},
	{4, "4"},
	{5, "5"},
	{6, "6"},
	{7, "7"},
	{8, "6"},
	{9, "9"},
	{10, "A"},
	{11, "B"},
	{12, "C"},
	{13, "D"},
	{14, "E"},
	{15, "F"}
};

std::vector<int> systems = {2, 8, 10, 16};

double keepDecimal(double val) {
	return val - static_cast<int>(val);
}

std::string convertSys (double value, int base, int precision) {
	std::string whole, fractional;
	
	int intval = value;
	while (intval > 0) {
		whole = symbols[intval % base] + whole;
		intval = intval / base;
	}
	
	double doubleval = keepDecimal(value);
	for (int i=0; i < precision; i++) {
		doubleval = base * keepDecimal(doubleval);
		fractional += symbols[static_cast<int>(doubleval)];
	}
	
	if (fractional == "") {
		return whole;
	}
	return whole + "." + fractional;
}

int randomint (int min, int max) {
	std::uniform_int_distribution<std::mt19937::result_type> dist(min, max);
	return dist(rng);
}
double randomdouble (double min, double max) {
	std::uniform_real_distribution<double> dist(min, max);
	return dist(rng);
}
std::vector<int> selectUniqueRandom (std::vector <int> vec, size_t howMany) {
	std::vector<int> selected;
	std::unordered_set<int> indexes;
	while (indexes.size() < howMany) {
		indexes.insert(randomint(0, vec.size()-1));
	}
	for (int i : indexes) {
		selected.push_back(vec[i]);
	}
	return selected;
}

void genQuestion() {
	double question = randomdouble(0.0, 1000.0);
	std::vector<int> bases = selectUniqueRandom(systems, 2);
	
	int prec_answer = randomint(0,5);
	int prec_question = std::ceil(prec_answer * log(bases[1]) / log(bases[0]));
	
	std::string converted = convertSys(question, bases[0], prec_question);
	std::string answer = convertSys(question, bases[1], prec_answer);
	std::cout << "Precision: " << prec_answer << '\n';
	std::cout << "Convert " << NumSysNames[bases[0]] << " " << converted << " to " << NumSysNames[bases[1]] << '\n';
	
	std::string toCheck = lineIn("Enter your answer: ");
	
	if (answer == toCheck) {
		std::cout << "Yes, your answer is correct" << '\n';
	} else {
		std::cout << "Incorrect answer. The correct answer was " << answer << '\n';
	}
}

int main(){
	
	while (true) {
		genQuestion();
		lineIn("", false);
	}
	
	return 0;
}






//	std::cout << convertSys(254.1234, 10, 4) << '\n';
//	std::vector<int> abc = {11, 22, 33, 44 ,55, 66, 77, 88, 99, 1010};
//	for (int i=0; i < 10; i++) {
//		std::vector<int> toPrint = selectUniqueRandom(abc, 10);
//		for (int i=0; i < toPrint.size(); i++) {
//			std::cout << toPrint[i] << ' ';
//		}
//		std::cout << '\n';
//	}
