
def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        a = str(a)
        b = str(b)
        result = a + b
    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# try:
#     #
#     # i = 0
#     # print(10/i)
#     # print('Done!')
# # except:
# #     print('Нельзя делить на 0')
#
# # try:
# #     tube = a + b
#     i = 0
#     # print(10/tube)
#     print(10/i)
#     print('Done!')
#
# except ZeroDivisionError as message_error:
#     print(f'Нельзя делить на 0, ошибка {message_error}')
#
# except NameError:
#     print('Что-то пошло не так')
#
# try:
#     file = open('blabla.txt')
#
# except OSError as exc:
#     print(f'Ошибка {exc}, параметры {exc.args}')
#
# else:
#     print("Удивительно, ошибок нет...")
#
# finally:
#     print("Несмотря на обстоятельства, мы завершили программу")
