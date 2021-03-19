import re

RE_VALID_MAIL = re.compile(r'(\w+)@([A-z0-9]+\.[A-z]{2,4})')

def email_parse(full_addr):
    try:
        assert RE_VALID_MAIL.match(full_addr)
    except AssertionError:
        raise ValueError(f'wrong email: {full_addr}')
    else:
        mail_data = RE_VALID_MAIL.findall(full_addr)
        return {'username': mail_data[0][0], 'domain': mail_data[0][1]}

print(email_parse('0055555@mail.ru'))
