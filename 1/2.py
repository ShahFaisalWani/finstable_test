def palindrome_check(user_input):
    word = str(user_input).lower()
    half_length = len(word) // 2

    for i in range(half_length):
        if word[i] != word[-i-1]:
            return False
    return True

while True:
    word = input("Enter word: ")
    is_palindrome = palindrome_check(word)
    print(f"{word} -> {is_palindrome}")