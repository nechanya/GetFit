_users = {
    'Masha': {
        'name': 'Masha Timoshenko',
        'weight': '56 kg',
        'height': '165 cm'
    },
    'Kate': {
        'name': 'Kate Novikova',
        'weight': '70 kg',
        'height': '160 cm'
    }
}


_user_list=[]

for login, user_data in _users.items():
    _new_element={'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)


def get_user(username):
    return _users.get(username)



def get_users_by_name(q):
    results= _user_list
    return results


