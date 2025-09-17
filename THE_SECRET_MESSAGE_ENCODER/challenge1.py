
def reverse_word(word):
    if len(word) <= 1:
        return word
    return word[-1] + word[:-1]

def main():
    input_str = input("Enter a string: ")
    words = input_str.split()
    rev_words = [reverse_word(word) for word in words]
    result = ' '.join(rev_words)
    print("Output:"  , result)
    


if __name__ == "__main__":
    main()
   

