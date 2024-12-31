import collections


def count_characters(text):
    text = text.lower()
    char_counts = collections.Counter(c for c in text if c.isalpha())
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


def count_words(text):
    words = text.split()
    return len(words)


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_counts = count_characters(file_contents)

    print(f'--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document\n')

    for char, count in char_counts:
        print(f"The '{char}' character was found {count} times")

    print('--- End report ---')


# Call the main function
if __name__ == "__main__":
    main()
