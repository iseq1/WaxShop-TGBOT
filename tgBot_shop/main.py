import telebot
import requests
from telebot import types
TOKEN = "token"
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

class Price:
    def __init__(self, price):
        self.price = price

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return self.price

class Type:
    def __init__(self, type):
        self.type = type

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

temp = Price(0)
tip = Type(0)

def GetCurse():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    CNY_rate = data['Valute']['CNY']['Value']
    return CNY_rate+0.1

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рассчитать стоимость')
    item2 = types.KeyboardButton('Срок доставки')
    item3 = types.KeyboardButton('Актульный курс')
    item4 = types.KeyboardButton('Действующие акции')
    item5 = types.KeyboardButton('Отзывы')
    item6 = types.KeyboardButton('Ответы на вопросы')
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'hi, {0.first_name}'.format(message.from_user), reply_markup= markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рассчитать стоимость':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Одежда')
            item2 = types.KeyboardButton('Обувь')
            item3 = types.KeyboardButton('Аксессуары')
            item4 = types.KeyboardButton('Другое')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, "Выберите тип вашего товара:", reply_markup=markup)

        elif message.text == 'Срок доставки':
            # выкуп + фромЧайна + фромСПБ
            bot.send_message(message.chat.id, "📦<b>Доставка📦</b>\n\n"
                                              "Выкуп товара с сайта Poizon 1-2 дня\n"
                                              "Доставка до нашего склада в китае 2-5 дней\n"
                                              "Складская обработка и отправка товара в РФ 1-3 дня\n"
                                              "Международная доставка до нашего склада 13-19 дней\n"
                                              "Отправка в ваш город курьерской службой CDEK 2-5 дней\n\n"
                                              "Среднее время доставки до нашего склада 17-25 дней. После оплаты вы сможете отслеживать статусы доставки и получать уведомления об их изменении.\n\n"
                                              "👮‍♂️<b>Безопасность</b> 👮‍♂\n\n"
                                              "В стоимость товара входит его полное страхование. Мы несем ответственность, чтобы вы получили свой заказ в целости и сохранности.\n\n"
                                              "🧾<b>Строго оригинал</b>🧾\n\n"
                                              "Мы гарантируем, что все купленные товары в Wax Shop оригинальные и прошли проверку на подлинность.")

        elif message.text == 'Актульный курс':
            bot.send_message(message.chat.id, f"Текущий обменный курс от CNY к RUB: <i>{GetCurse()}</i>")


        elif message.text == 'Действующие акции':
            bot.send_message(message.chat.id, 'Акция для любителей оригинальной продукции:\n'
                                              '•Подарок при первом заказе🎁 \n'
                                              '•Подарок за каждого приведенного друга при следующем заказе🎁 \n'
                                              'Друг так же не останется без поощрения и получит скидку -10% на комиссию нашего сервиса🤑')

        elif message.text == 'Отзывы':
            bot.send_message(message.chat.id, '📣<b>Отзыв</b> о вашем товаре, его состоянии и качестве обслуживания вы можете <b>оставить тут</b>: @wax_review')

        elif message.text == 'Ответы на вопросы':
            bot.send_message(message.chat.id, '⁉️<b>Задать</b> все интересующие вас вопросы вы можете нашему <b>администратору</b> @order_wax_shop')

        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Рассчитать стоимость')
            item2 = types.KeyboardButton('Срок доставки')
            item3 = types.KeyboardButton('Актульный курс')
            item4 = types.KeyboardButton('Действующие акции')
            item5 = types.KeyboardButton('Отзывы')
            item6 = types.KeyboardButton('Ответы на вопросы')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, "Назад", reply_markup=markup)

        elif message.text == "Одежда":
            tip.setType(1)
            calculate_price_step_one(message.chat.id)

        elif message.text == "Обувь":
            tip.setType(2)
            calculate_price_step_one(message.chat.id)

        elif message.text == "Аксессуары":
            tip.setType(3)
            calculate_price_step_one(message.chat.id)

        elif message.text == "Другое":
            tip.setType(4)
            calculate_price_step_one(message.chat.id)

        elif  any(char.isdigit() for char in message.text) and tip.getType()!=0:
            try:
                price = float(message.text)
                temp.setPrice(price)
                type_of_choise(message.chat.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Рассчитать стоимость')
                item2 = types.KeyboardButton('Срок доставки')
                item3 = types.KeyboardButton('Актульный курс')
                item4 = types.KeyboardButton('Действующие акции')
                item5 = types.KeyboardButton('Отзывы')
                item6 = types.KeyboardButton('Ответы на вопросы')
                markup.add(item1, item2, item3, item4, item5, item6)
            except ValueError:
                bot.send_message(message.chat.id, "Некорректное сообщение. Пожалуйста, введите число.")

        else:
            bot.send_message(message.chat.id, "Некорректное сообщение")



def calculate_price_step_one(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    x = tip.getType()
    if x == 1:
        media = [
            types.InputMediaPhoto(open('D:/projects/Python/tgBot_shop/clother1.jpg', 'rb'), caption=''),
            types.InputMediaPhoto(open('D:/projects/Python/tgBot_shop/clother2.jpg', 'rb'), caption='')
        ]
        bot.send_media_group(chat_id, media)
        bot.send_message(chat_id, "💵<b>Отправьте мне цену за позицию в ¥ для расчёта</b>💵", reply_markup=markup)

    elif x == 2:
        media = [
            types.InputMediaPhoto(open('D:/projects/Python/tgBot_shop/shoes1.jpg', 'rb'), caption=''),
            types.InputMediaPhoto(open('D:/projects/Python/tgBot_shop/shoes2.jpg', 'rb'), caption='')
        ]
        bot.send_media_group(chat_id, media)
        bot.send_message(chat_id, "💵<b>Отправьте мне цену за позицию в ¥ для расчёта</b>💵", reply_markup=markup)

    elif x == 3:
        media = [
            types.InputMediaPhoto(open('D:/projects/Python/tgBot_shop/acsesuar1.jpg', 'rb'), caption=''),
            types.InputMediaPhoto(open('D:/projects/Python/tgBot_shop/acsesuar2.jpg', 'rb'), caption='')
        ]
        bot.send_media_group(chat_id, media)
        bot.send_message(chat_id, "💵<b>Отправьте мне цену за позицию в ¥ для расчёта</b>💵", reply_markup=markup)

    else:
        bot.send_message(chat_id, "💵<b>Отправьте мне цену за позицию в ¥ для расчёта</b>💵", reply_markup=markup)


def type_of_choise(chat_id):
    x = tip.getType()
    if x == 1:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Рассчитать стоимость')
        item2 = types.KeyboardButton('Срок доставки')
        item3 = types.KeyboardButton('Актульный курс')
        item4 = types.KeyboardButton('Действующие акции')
        item5 = types.KeyboardButton('Отзывы')
        item6 = types.KeyboardButton('Ответы на вопросы')
        markup.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(chat_id, f"📈Результат: {round(temp.getPrice() * GetCurse() + 2549, 1)} \n\n"
                                          f"¥ =  {GetCurse()}\n\n"
                                          "⚖️Формула для выбранной категории\n\n"
                                          "Категория товара: Одежда\n"
                                          f"- {(int)(temp.getPrice())} * 12.71 + (750 + 800 + 999)\n"
                                          "- Цена * курс + (доставка по Китаю + Китай - Склад + комиссия сервиса)\n\n"
                                          "💰Готов оформить заказ или задать вопрос ?\n"
                                          "Тебе сюда: @order_wax_shop\n\n"
                                          "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 👨‍💼\n\n"
                                          "Все заказы оформляются только через @order_wax_shop", reply_markup=markup)
    if x == 2:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Рассчитать стоимость')
        item2 = types.KeyboardButton('Срок доставки')
        item3 = types.KeyboardButton('Актульный курс')
        item4 = types.KeyboardButton('Действующие акции')
        item5 = types.KeyboardButton('Отзывы')
        item6 = types.KeyboardButton('Ответы на вопросы')
        markup.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(chat_id, f"📈Результат: {round(temp.getPrice() * GetCurse() + 2599, 1)} \n\n"
                                          f"¥ =  {GetCurse()}\n\n"
                                          "⚖️Формула для выбранной категории\n\n"
                                          "Категория товара: Обувь\n"
                                          f"- {(int)(temp.getPrice())} * 12.71 + (800 + 800 + 999)\n"
                                          "- Цена * курс + (доставка по Китаю + Китай - Склад + комиссия сервиса)\n\n"
                                          "💰Готов оформить заказ или задать вопрос ?\n"
                                          "Тебе сюда: @order_wax_shop\n\n"
                                          "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 👨‍💼\n\n"
                                          "Все заказы оформляются только через @order_wax_shop", reply_markup=markup)
    if x == 3:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Рассчитать стоимость')
        item2 = types.KeyboardButton('Срок доставки')
        item3 = types.KeyboardButton('Актульный курс')
        item4 = types.KeyboardButton('Действующие акции')
        item5 = types.KeyboardButton('Отзывы')
        item6 = types.KeyboardButton('Ответы на вопросы')
        markup.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(chat_id, f"📈Результат: {round(temp.getPrice() * GetCurse() + 2499, 1)} \n\n"
                                          f"¥ =  {GetCurse()}\n\n"
                                          "⚖️Формула для выбранной категории\n\n"
                                          "Категория товара: Аксессуары\n"
                                          f"- {(int)(temp.getPrice())} * 12.71 + (700 + 800 + 999)\n"
                                          "- Цена * курс + (доставка по Китаю + Китай - Склад + комиссия сервиса)\n\n"
                                          "💰Готов оформить заказ или задать вопрос ?\n"
                                          "Тебе сюда: @order_wax_shop\n\n"
                                          "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 👨‍💼\n\n"
                                          "Все заказы оформляются только через @order_wax_shop", reply_markup=markup)
    if x == 4:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Рассчитать стоимость')
        item2 = types.KeyboardButton('Срок доставки')
        item3 = types.KeyboardButton('Актульный курс')
        item4 = types.KeyboardButton('Действующие акции')
        item5 = types.KeyboardButton('Отзывы')
        item6 = types.KeyboardButton('Ответы на вопросы')
        markup.add(item1, item2, item3, item4, item5, item6)
        bot.send_message(chat_id, f"📈Результат: {round(temp.getPrice() * GetCurse() + 2599, 1)} \n\n"
                                          f"¥ =  {GetCurse()}\n\n"
                                          "⚖️Формула для выбранной категории\n\n"
                                          "Категория товара: Аксессуары\n"
                                          f"- {(int)(temp.getPrice())} * 12.71 + (800 + 800 + 999)\n"
                                          "- Цена * курс + (доставка по Китаю + Китай - Склад + комиссия сервиса)\n\n"
                                          "💰Готов оформить заказ или задать вопрос ?\n"
                                          "Тебе сюда: @order_wax_shop\n\n"
                                          "Для оформления заказа отправь фотографию товара, ссылку и свой размер менеджеру 👨‍💼\n\n"
                                          "Все заказы оформляются только через @order_wax_shop", reply_markup=markup)


bot.polling(none_stop=True)


