def expanded_form(num):
    # Разделяем число на целую и дробную части
    integer_part, decimal_part = str(num).split('.')
    
    # Обрабатываем целую часть
    integer_expanded = [
        str(int(digit) * 10**i)
        for i, digit in enumerate(reversed(integer_part))
        if digit != '0'
    ]
    integer_expanded.reverse()  # Приводим порядок в нормальный вид
    
    # Обрабатываем дробную часть
    decimal_expanded = [
        f"{digit}/{10**(i + 1)}"
        for i, digit in enumerate(decimal_part)
        if digit != '0'
    ]
    
    # Объединяем обе части
    expanded = integer_expanded + decimal_expanded
    return " + ".join(expanded)

# Примеры использования
print(expanded_form(807.304))  # Вывод: "800 + 7 + 3/10 + 4/1000"
print(expanded_form(1.24))    # Вывод: "1 + 2/10 + 4/100"
print(expanded_form(7.304))   # Вывод: "7 + 3/10 + 4/1000"
print(expanded_form(0.04))    # Вывод: "4/100"