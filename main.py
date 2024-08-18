def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_characters(text):
    character_dict= {}

    for letter in text.lower():
        if letter in character_dict:
            character_dict[letter] += 1
        else :
            character_dict[letter] = 1

    return character_dict

main() 

