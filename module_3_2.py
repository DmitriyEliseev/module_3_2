def send_email (message,recipient,sender="university.help@gmail.com"):
    global message_out
    message_out=""
    if sender.count("@")==0 or recipient.count("@")==0:
        message_out = "Невозможно отправить писмо с адреса "+sender+" на адрес"+recipient
        return message_out

    if sender.find(".com",len(sender)-4,) <0 and \
            sender.find(".net", len(sender) - 4, ) < 0 and \
            sender.find(".ru", len(sender) - 3, ) < 0:
        message_out = "Невозможно отправить письмо с адреса "+sender +" на адрес "+ recipient
        return message_out

    if recipient.find(".com",len(recipient)-4,) <0 and \
            recipient.find(".net", len(recipient) - 4, ) < 0 and \
            recipient.find(".ru", len(recipient) - 3, ) < 0:
            message_out = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient
            return message_out

    if sender==recipient:
        message_out ="Нельзя отправить письмо самому себе!"
        return message_out

    if sender ==("university.help@gmail.com"):

        message_out ="Письмо успешно отправлено с адреса "+ sender + "на адрес " + recipient
        return message_out

    else:
        message_out = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса " + sender + " на адрес " + recipient
        return message_out


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print (message_out)
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print (message_out)
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print (message_out)
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print (message_out)