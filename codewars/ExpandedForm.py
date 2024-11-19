def expanded_form(num):
    result = []
    place_value = 1

    while num > 0:
        digit = num % 10  # Получаем последнюю цифру
        if digit != 0:
            expanded_part = str(digit * place_value)
            result.insert(0, expanded_part)  # Добавляем развернутую часть в начало списка
        num //= 10  # Убираем последнюю цифру
        place_value *= 10  # Переходим к следующему разряду

    return " + ".join(result)
