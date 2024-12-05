def array():
    data = []

    def get_item(index):
        return data[index] if 0 <= index < len(data) else None

    def push_item(value):
        data.append(value)

    def pop_item():
        return data.pop() if data else None

    return lambda action=None, *args: {
        "get": lambda index: get_item(index),
        "push": lambda value: push_item(value),
        "pop": lambda: pop_item(),
    }.get(action, lambda *a: None)(*args)


# Пример использования:
arr = array()

# Добавляем элементы
arr("push", "first")
arr("push", "second")
arr("push", "third")

# Доступ к элементам по индексу
print(arr("get", 0))  # Выводит: first
print(arr("get", 1))  # Выводит: second
print(arr("get", 2))  # Выводит: third

# Удаление элементов (pop)
print(arr("pop"))  # Выводит: third
print(arr("pop"))  # Выводит: second
print(arr("pop"))  # Выводит: first
print(arr("pop"))  # Выводит: None
