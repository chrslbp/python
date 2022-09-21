"""Here is the implementation of the password security check"""

import string


def password_strength(value: str) -> str:
    """
    Функция проверки пароля.
    Условия проверки:
    - если пароль короче 8 символов, то вернуть "Too Weak"
    - если пароль содержит только цифры, только строчные или только заглавные буквы, то вернуть Weak
    - если пароль содержит символы любых 2 наборов, то вернуть Good
    - если пароль содержит 3 наборов, то вернуть Very Good
    """
    if len(value)<8:
        return 'Too Weak'

    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    count = 0

    for symbol in (digits, lowers, uppers):
        if any(e in symbol for e in value):
            count += 1

    if count == 3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'

# testing
if __name__ == '__main__':
    # если пароль короче 8 символов, то вернуть "Too Weak"
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('asdfghw') == 'Too Weak'
    assert password_strength('ASDFGHE') == 'Too Weak'
    assert password_strength('asdASDc') == 'Too Weak'

    # если пароль содержит только цифры, только строчные или только заглавные буквы, то вернуть Weak
    assert password_strength('12345678') == 'Weak'
    assert password_strength('asdfghjk') == 'Weak'
    assert password_strength('1234567890') == 'Weak'
    assert password_strength('ASDFGHWJ') == 'Weak'
    assert password_strength('ASDFGHREW') == 'Weak'

    # если пароль содержит символы любых 2 наборов, то вернуть Good
    assert password_strength('1234asdf') == 'Good'
    assert password_strength('1234ASDF') == 'Good'
    assert password_strength('asdfQWER') == 'Good'
    assert password_strength('1234asdfa') == 'Good'
    assert password_strength('12345asdf') == 'Good'

    # если пароль содержит 3 наборов, то вернуть Very Good
    assert password_strength('123456aS') == 'Very Good'
    assert password_strength('6aSasdfg') == 'Very Good'
    assert password_strength('ASDFGH4w') == 'Very Good'
    assert password_strength('asdfghH2') == 'Very Good'

