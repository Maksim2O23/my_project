def uppercase_string(input_string):
    """
    Преобразует входную строку в верхний регистр.

    Args:
        input_string (str): Входная строка для преобразования.

    Returns:
        str: Строка в верхнем регистре.
    """
    return input_string.upper()

def capitalize_words(input_string):
    """
    Преобразует входную строку, делая заглавными первые буквы каждого слова.

    Args:
        input_string (str): Входная строка для преобразования..

    Returns:
        str: Строка с заглавными первыми буквами каждого слова.
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

