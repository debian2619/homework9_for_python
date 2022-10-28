def string_counter():
    with open('phonebook.txt') as phonebook:
        last_used_id = 0
        for i in phonebook:
            last_used_id = int(i.split('**')[0])
    return last_used_id


def create_note(new_note_list):
    with open('phonebook.txt', 'a+', encoding='utf-8') as phonebook:
        id = string_counter() + 1
        last_name = new_note_list[0]
        first_name = new_note_list[1]
        phone_number = new_note_list[2]
        comment = new_note_list[3]
        phonebook.write(
            f'\n{id}**{last_name}**{first_name}**{phone_number}**{comment}')


def delete_note(id_to_del):
    temp = ''
    with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
        for i in phonebook:
            if i.split('**')[0] != id_to_del:
                temp += i
    with open('phonebook.txt', 'w', encoding='utf-8') as phonebook:
        phonebook.write(temp)