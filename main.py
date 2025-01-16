def main(book):
    with open(book) as f:
        file_contents = f.read()
        print(file_contents)

def word_count(book):
    count = 0
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
    print(f"There are {count} words in this document")
    return count
    
def character_count(book):
    with open(book) as f:
        file_contents = f.read()
        characters = file_contents.replace(" ", "").lower()
    occurence = {}
    for c in characters:
        if c.isalpha() == False:
            pass
        elif c not in occurence:
            occurence[c] = 1
        else:
            occurence[c] += 1
    return occurence

def report(book):
    print(f"--- Begin report of {book} ---")
    print()
    word_count(book)
    print()
    count = character_count(book)

    for key in count:
        print(f"The '{key}' character appeared {count[key]} times")


report("books/frankenstein.txt")