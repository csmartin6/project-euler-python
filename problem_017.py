num2word={1: "one",2: "two", 3:"three",4:"four",5:"five",
		6:"six", 7:"seven", 8:"eight", 9:"nine", 10: "ten", 
		11:"eleven", 12: "twelve", 13:"thirteen", 14:"fourteen",
		15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
		19: "nineteen",20: "twenty", 30: "thirty", 40:"forty",
		50: "fifty", 60:"sixty", 70: "seventy", 80:"eighty",90: "ninety"}
N = 1001

def convertNumberToWords(num):
	if num in num2word:
		return num2word[num]

	if num >=1000:
		return convertNumberToWords(num/1000)+" thousand" + \
		(" and "+convertNumberToWords(num%1000) if num%1000 else "")
	elif num >=100:
		return convertNumberToWords(num/100)+" hundred" + \
		(" and "+convertNumberToWords(num%100) if num%100 else "")
	elif num > 20:
		return convertNumberToWords(num-num%10)+ \
		(" "+convertNumberToWords(num%10) if num%10 else "")
	else: 
		raise RuntimeError("Something has gone wrong")

def letterCount(num_word):
	return len(num_word.replace(" ",""))

letters = 0
for i in xrange(1,N):
	num_word = convertNumberToWords(i)
	letters += letterCount(num_word)


print letters
