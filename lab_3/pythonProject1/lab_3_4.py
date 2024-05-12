phrase = str(input('Введите сообщение на английском языке: '))

lengthPrase = len(phrase)
print(lengthPrase)

lowerPhrase = phrase.lower()
print(lowerPhrase)

a_count = lowerPhrase.count('a')
print('Количество буквы "а" в предложении: ', a_count)

e_count = lowerPhrase.count('e')
print('Количество буквы "e" в предложении: ', e_count)

i_count = lowerPhrase.count('i')
print('Количество буквы "i" в предложении: ', i_count)

o_count = lowerPhrase.count('o')
print('Количество буквы "o" в предложении: ', o_count)

u_count = lowerPhrase.count('u')
print('Количество буквы "u" в предложении: ', u_count)

if 'ugly' in lowerPhrase:
    replacePhrase = lowerPhrase.replace('ugly', 'beauty')
    print('Программа заменила триггер-слово на приемлимое: ' + replacePhrase)

startPhrase = lowerPhrase.startswith('the')
if startPhrase == 1:
    print('Предложение начинается с the')

endPhrase = lowerPhrase.endswith('end')
if endPhrase == 1:
    print('Предложение оканчивается на end')
