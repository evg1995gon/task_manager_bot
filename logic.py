import db

def parsing_massage(text_message, id):
    parsed = text_message.split(" ")[0]
    if len(text_message.split(" ")) > 1:
        second = text_message.split(" ")[1]
    begining = " ".join(text_message.split(" ")[1:])
    id_of_the_author = db.get_id(id)
    if parsed.lower() == 'добавить':
        db.add_task(begining, id_of_the_author)
        return f"'{begining}'" + " было добавленно в список ваших целей "
    elif parsed.lower() == 'удалить' and (second.lower() == 'все' or second.lower() =='всё'):
        db.delete_all(id)
    elif parsed.lower() == 'список':
        list_of = db.list_of_tasks(id_of_the_author)
        return list_of
    elif parsed.lower() == 'удалить':
        if begining in db.list_of_all_messages():
            db.delete_task(begining)
            return f"цель '{begining}' успешна удалина из вашего списка"
        else:
            return f"Цели '{begining}' не было найдено"
    else:
        return "используйте вначале слово 'добавить ...', 'удалить ...' или 'список'"

def add_member(id, user):
    list_of_users = db.select_users()
    if id in list_of_users:
        pass
    else:
        db.add_member(id, user)
