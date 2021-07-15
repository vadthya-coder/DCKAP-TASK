def small_numbers(number):
    number_in_english = ""
    if  number >= 100 and number < 1000:
        tens = number // 100
        number = number % 100
        number_in_words = below_19_list[tens-1]
        number_in_english += number_in_words + " " + "hundred "
    if number>=20 and number<100:
        tens = number // 10 
        number = number % 10 
        number_in_words = tens_list[tens-2]
        number_in_english += number_in_words + " "
    if number !=0 and number < 20:
        number_in_words = below_19_list[number-1]
        number_in_english += number_in_words + " "
    return number_in_english
def big_number(number):
    number_in_english = ''
    if number >= 1000000000 and number <= 10000000000:
        req = number // 1000000000
        number = number % 1000000000
        number_in_words = small_numbers(req)
        number_in_english += number_in_words +"billion "
    if number >=1000000 and number < 1000000000:
        req = number // 1000000 
        number = number % 1000000
        number_in_words = small_numbers(req)
        number_in_english += number_in_words + "million "
    if number >= 1000 and number < 1000000:
        req = number // 1000 
        number = number % 1000 
        number_in_words = small_numbers(req)
        number_in_english += number_in_words + "thousand "
    if number > 0 and number < 1000:
        number_in_english +=small_numbers(number)
    
    return number_in_english

number = int(input())
if number==1:
    print("one dollar")
elif number==0:
    pass
else:
    number_in_english = ''
    below_19_list= ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_list = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    number_in_english = big_number(number)
    print(number_in_english+" dollars")