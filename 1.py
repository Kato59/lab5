def seq(*functions):
    def chained_function(value):
        for func in functions:
            value = func(value)
        return value
    return chained_function

# Примеры использования:
result1 = seq(lambda x: x + 7, lambda x: x * 2)(5)
print(result1)  # Результат: 17

result2 = seq(lambda x: x * 2, lambda x: x + 7)(5)
print(result2)  # Результат: 24

result3 = seq(lambda x: x + 1, lambda x: x * 2, lambda x: x // 3, lambda x: x - 4)(7)
print(result3)  # Результат: 3
