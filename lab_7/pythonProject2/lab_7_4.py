def load_censor(file_name):
    with open(file_name, 'r') as file:
        censor_words = file.read().split()
    return censor_words

def censor(text, censor_words):
    censor_text = text
    for word in censor_words:
        censored_word = '*' * len(word)
        censor_text = censor_text.replace(word.lower(), censored_word)
        censor_text = censor_text.replace(word.capitalize(), censored_word)
        censor_text = censor_text.replace(word.upper(), censored_word)
    return censor_text

def main():
    censor_words = load_censor("input1.txt")
    text = input("Введите предложение: ")
    censored_text = censor(text, censor_words)
    print("Результат: ", censored_text)

if __name__ == "__main__":
    main()