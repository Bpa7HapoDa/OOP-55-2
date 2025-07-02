# def square_result(func):
#
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result ** 2
#     return wrapper
#
# @square_result
# def add(a, b):
#
#     return a + b
#
# print(add(2, 3))

def check_user(user):

    def decorator(func):
        def wrapper():
            if user == "admin":
                return func()
            else:
                print("Доступ запрещен. Только для admin.")
        return wrapper
    return decorator

@check_user("admin")
def delete_database():
    print("База данных удалена!")

delete_database()

@check_user("person")
def delete_logs():
   print("Логи удалены!")

delete_logs()
