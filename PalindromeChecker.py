def is_palindrome_for(input_string: str) -> bool:

    input_string = ''.join(c for c in input_string if c.isalnum()).lower()


    length = len(input_string)


    for i in range(length // 2):
        if input_string[i] != input_string[length - 1 - i]:
            return False

    return True

print(is_palindrome_for("A man, a plan, a canal, Panama"))