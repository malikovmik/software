def count_unique_words(file_name):
    unique_words = set()
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            words = line.strip().split()
            unique_words.update(words)
    return unique_words


def main():
    file_name = "text.txt"
    unique_words = count_unique_words(file_name)
    sorted_unique_words = sorted(unique_words)

    print("Уникальные слова в тексте:")
    for word in sorted_unique_words:
        print(word)


if __name__ == "__main__":
    main()
