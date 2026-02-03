from random import randint, choices
import string


def print_hi(name: str = 'PyCharm'):
    print(f'Hi, {name}')

# функция для генерации email
def generator_email(user_name: str = None) -> str:
    if user_name is None:
        user_name = ''.join(choices(string.ascii_letters, k=10, ))

    return f'{user_name}{randint(10, 999)}@gmail.com'



if __name__ == '__main__':
    print_hi('Георгий')
    print_hi('GUAP')


    text = "*" * 12
    print_hi('PyCharm')
    print_hi(text)