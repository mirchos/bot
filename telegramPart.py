import telebot


def send_message(data, chat_id=-433129876):  # chat_id=-433129876 - id тестового чата
    token = '1157251949:AAGB06yVhRJ2PDOHpPDB8g9YzAledqruBXM'
    bot = telebot.TeleBot(token)
    bot.send_message(chat_id, data)


def main():
    send_message("test")


if __name__ == '__main__':
    main()
