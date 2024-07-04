def send_email(message, recipient, sender="university.help@gmail.com"):
    corr_recipient = '@' in recipient and (recipient.endswith('.com')
                                           or recipient.endswith('.ru')
                                           or recipient.endswith('.net'))
    corr_sender = '@' in sender and (sender.endswith('.com')
                                     or sender.endswith('.ru')
                                     or sender.endswith('.net'))
    if corr_recipient and corr_sender:
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        else:
            if sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
            else:
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    else:
         print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')

