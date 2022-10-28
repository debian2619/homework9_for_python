def print_note(id, sep: str):
    check = 0
    with open('phonebook.txt') as phonebook:
        for i in phonebook:
            if i.split('**')[0] == id:
                check = 1
                return (sep.join(i.split('**')))
    if check == 0:
        return('Такой записи нет')


def print_phonebook(sep: str):
    output = ''
    with open('phonebook.txt') as phonebook:
        for i in phonebook:
            output += (sep.join(i.split('**')))
    return output