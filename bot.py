import telebot
import config
import random

from telebot import types
import test
bot = telebot.TeleBot(config.TOKEN)

 
@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    item2 = types.InlineKeyboardButton("Контактная информация РПЧСИ", callback_data='main2',url="https://zhso.kz/index.php?view=catalog&main_cat=2&cat_id=12")
    item3 = types.InlineKeyboardButton("Запись на прием граждан", callback_data='main3')
    item4 = types.InlineKeyboardButton("Законы", callback_data='main4')
    item5 = types.InlineKeyboardButton("Рейтинг ЧСИ", callback_data='main5',url="https://aisoip.adilet.gov.kz/forCitizens/ratingLawmen")
    item6 = types.InlineKeyboardButton("Реестр должников", callback_data='main6',url="https://aisoip.adilet.gov.kz/debtors")
    item7 = types.InlineKeyboardButton("Инструкции", callback_data='main7')
    item8 = types.InlineKeyboardButton("Часто задаваемые вопросы", callback_data='main8')
    item9 = types.InlineKeyboardButton("Подать обращение в МЮ РК", callback_data='main9',url="https://egov.kz/wps/myportal/Esedo")
    item10 = types.InlineKeyboardButton("Блог Министра юстиции РК", callback_data='main10',url="https://dialog.egov.kz/blogs/32772/welcome")
    item11 = types.InlineKeyboardButton("Проверьте свои аресты", callback_data='main11',url='https://aisoip.adilet.gov.kz/forCitizens/findArest')
 
    markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, ТЕСТОВЫЙ бот Департамента исполнения судебных актов МЮ РК".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    test.do(message.from_user.first_name)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        # keyboard
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        item2 = types.InlineKeyboardButton("Контактная информация РПЧСИ", callback_data='main2',url="https://zhso.kz/index.php?view=catalog&main_cat=2&cat_id=12")
        item3 = types.InlineKeyboardButton("Запись на прием граждан", callback_data='main3')
        item4 = types.InlineKeyboardButton("Законы", callback_data='main4')
        item5 = types.InlineKeyboardButton("Рейтинг ЧСИ", callback_data='main5',url="https://aisoip.adilet.gov.kz/forCitizens/ratingLawmen")
        item6 = types.InlineKeyboardButton("Реестр должников", callback_data='main6',url="https://aisoip.adilet.gov.kz/debtors")
        item7 = types.InlineKeyboardButton("Инструкции", callback_data='main7')
        item8 = types.InlineKeyboardButton("Часто задаваемые вопросы", callback_data='main8')
        item9 = types.InlineKeyboardButton("Подать обращение в МЮ РК", callback_data='main9',url="https://egov.kz/wps/myportal/Esedo")
        item10 = types.InlineKeyboardButton("Блог Министра юстиции РК", callback_data='main10',url="https://dialog.egov.kz/blogs/32772/welcome")
        item11 = types.InlineKeyboardButton("Проверьте свои аресты", callback_data='main11',url='https://aisoip.adilet.gov.kz/forCitizens/findArest')
 		
        markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
        bot.send_message(message.chat.id, 'Выберите один из нижеперечисленных вариантов!', reply_markup=markup)
        test.do(message.from_user.first_name)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'main3':
                markup = types.InlineKeyboardMarkup(row_width=1)

                item1 = types.InlineKeyboardButton("ДЮ города Нур-Султан",url="https://www.gov.kz/memleket/entities/adilet-nur-sultan/activities/appointment-schedule?lang=ru")
                item2 = types.InlineKeyboardButton("ДЮ города Алматы",url="https://www.gov.kz/memleket/entities/adilet-almaty/activities/appointment-schedule?lang=ru")
                item3 = types.InlineKeyboardButton("ДЮ города Шымкент",url="https://www.gov.kz/memleket/entities/adilet-shymkent/activities/appointment-schedule?lang=ru")
                item4 = types.InlineKeyboardButton("ДЮ Актюбинской области",url="https://www.gov.kz/memleket/entities/adilet-akt/activities/appointment-schedule?lang=ru")
                item5 = types.InlineKeyboardButton("ДЮ Туркестанской области",url="https://www.gov.kz/memleket/entities/adilet-trk/activities/appointment-schedule?lang=ru")
                item6 = types.InlineKeyboardButton("ДЮ Кызылординской области",url="https://www.gov.kz/memleket/entities/adilet-kzl/activities/appointment-schedule?lang=ru")
                item7 = types.InlineKeyboardButton("ДЮ Северо-Казахстанской области",url="https://www.gov.kz/memleket/entities/adilet-sko/activities/appointment-schedule?lang=ru")
                item8 = types.InlineKeyboardButton("ДЮ Павлодарской области",url="https://www.gov.kz/memleket/entities/adilet-pvl/activities/appointment-schedule?lang=ru")
                item9 = types.InlineKeyboardButton("ДЮ Восточно-Казахстанской области",url="https://www.gov.kz/memleket/entities/adilet-shko/activities/appointment-schedule?lang=ru")
                item10 = types.InlineKeyboardButton("ДЮ Мангистауской области",url="https://www.gov.kz/memleket/entities/adilet-mng/activities/appointment-schedule?lang=ru")
                item11 = types.InlineKeyboardButton("ДЮ Акмолинской области",url="https://www.gov.kz/memleket/entities/adilet-akm/activities/appointment-schedule?lang=ru")
                item12 = types.InlineKeyboardButton("ДЮ Алматинской области",url="https://www.gov.kz/memleket/entities/adilet-alm/activities/appointment-schedule?lang=ru")
                item13 = types.InlineKeyboardButton("ДЮ Атырауской области",url="https://www.gov.kz/memleket/entities/adilet-atr/activities/appointment-schedule?lang=ru")
                item14 = types.InlineKeyboardButton("ДЮ Западно-Казахстанской области",url="https://www.gov.kz/memleket/entities/adilet-bko/activities/appointment-schedule?lang=ru")
                item15 = types.InlineKeyboardButton("ДЮ Жамбылской области",url="https://www.gov.kz/memleket/entities/adilet-zhmb/activities/appointment-schedule?lang=ru")
                item16 = types.InlineKeyboardButton("ДЮ Карагандинской области",url="https://www.gov.kz/memleket/entities/adilet-krg/activities/appointment-schedule?lang=ru")
                item17 = types.InlineKeyboardButton("ДЮ Костанайской области",url="https://www.gov.kz/memleket/entities/adilet-kst/activities/appointment-schedule?lang=ru")
                item18 = types.InlineKeyboardButton("Республиканская палата ЧСИ", url='https://zhso.kz/index.php?view=catalog&cat_id=16')
                item19 = types.InlineKeyboardButton("Назад", callback_data='cancel')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19 )
                bot.send_message(call.message.chat.id, 'Выберите нужное из списка', reply_markup=markup)



            elif call.data == 'main4':
                markup = types.InlineKeyboardMarkup(row_width=1)

                item1 = types.InlineKeyboardButton("Гражданский кодекс Республики Казахстан (Общая часть)",url="http://adilet.zan.kz/rus/docs/K940001000_")
                item2 = types.InlineKeyboardButton("Гражданский кодекс Республики Казахстан (Особенная часть)",url="http://adilet.zan.kz/rus/docs/K990000409_")
                item3 = types.InlineKeyboardButton("Гражданский процессуальный кодекс Республики Казахстан",url="http://adilet.zan.kz/rus/docs/K1500000377")
                item4 = types.InlineKeyboardButton("Уголовный кодекс Республики Казахстан ",url="http://adilet.zan.kz/rus/docs/K1400000226")
                item5 = types.InlineKeyboardButton("Уголовно-процессуальный кодекс Республики Казахстан",url="http://adilet.zan.kz/rus/docs/K1400000231")
                item6 = types.InlineKeyboardButton("Кодекс Республики Казахстан об административных правонарушениях",url="http://adilet.zan.kz/rus/docs/K1400000235")
                item7 = types.InlineKeyboardButton("Предпринимательский кодекс Республики Казахстан",url="http://adilet.zan.kz/rus/docs/K1500000375")
                item8 = types.InlineKeyboardButton("Кодекс Республики Казахстан о браке (супружестве) и семье",url="http://adilet.zan.kz/rus/docs/K1100000518")
                item9 = types.InlineKeyboardButton("Об исполнительном производстве и статусе судебных исполнителей",url="http://adilet.zan.kz/rus/docs/Z100000261_")
                item10 = types.InlineKeyboardButton("О банках и банковской деятельности в Республике Казахстан",url="http://adilet.zan.kz/rus/docs/Z950002444_")
                item11 = types.InlineKeyboardButton("О правовых актах",url="http://adilet.zan.kz/rus/docs/Z1600000480")
                item12 = types.InlineKeyboardButton("О пенсионном обеспечении в Республике Казахстан",url="http://adilet.zan.kz/rus/docs/Z1300000105")
                item13 = types.InlineKeyboardButton("Назад", callback_data='cancel')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
                bot.send_message(call.message.chat.id, 'Выберите Закон', reply_markup=markup)


            elif call.data == 'yes':
                text = "Ваше обращение принято к рассмотрению!\nОтвет будет дан в соответствии с Законом Республики Казахстан"
                bot.send_message(call.message.chat.id, text)
                
                
                
                #Заполнить в базу

            elif call.data == 'main7':
            	markup = types.InlineKeyboardMarkup(row_width=1)
            	item1 = types.InlineKeyboardButton("Выписка ОПВ с параметрами, ОПВ выплаты с параметром", callback_data='file1')
            	item2 = types.InlineKeyboardButton("Инструкция по взысканию в солидарном порядке", callback_data='file2')
            	item3 = types.InlineKeyboardButton("Инструкция по заполнению банковских реквизитов", callback_data='file3')
            	item4 = types.InlineKeyboardButton("Инструкция по использованию ЭЦП", callback_data='file4')
            	item5 = types.InlineKeyboardButton("Инструкция по наложению (снятию, приостановлению) запрета на выезд должника из РК", callback_data='file5')
            	item6 = types.InlineKeyboardButton("Инструкция по редактированию и.п.", callback_data='file6')
            	item8 = types.InlineKeyboardButton("Назад", callback_data='cancel')
            	markup.add(item1, item2, item3, item4, item5, item6, item8)
            	bot.send_message(call.message.chat.id, 'Выберите нужное из списка', reply_markup=markup)

            elif call.data == 'cancel':
            	bot.delete_message(call.message.chat.id, call.message.message_id)

            elif call.data =='file1':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	f = open("file1.pdf","rb")
            	bot.send_document(call.message.chat.id,f)
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data =='file2':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	f = open("file2.pdf","rb")
            	bot.send_document(call.message.chat.id,f)
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data =='file3':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	f = open("file3.pdf","rb")
            	bot.send_document(call.message.chat.id,f)
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data =='file4':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	f = open("file4.pdf","rb")
            	bot.send_document(call.message.chat.id,f)
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data =='file5':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	f = open("file5.pdf","rb")
            	bot.send_document(call.message.chat.id,f)
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data =='file6':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	f = open("file6.pdf","rb")
            	bot.send_document(call.message.chat.id,f)
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data == 'main8':
            	markup = types.InlineKeyboardMarkup(row_width=1)
            	item1 = types.InlineKeyboardButton("Что делать в случае наложения ареста ЧСИ на Ваши расчетные счета в банках второго уровня?",callback_data='ans1')
            	item2 = types.InlineKeyboardButton("Как и куда можно предъявить исполнительный документ на исполнении к судебному исполнителю? ",callback_data='ans2')
            	item3 = types.InlineKeyboardButton("Как можно узнать какие исполнительные производства возбуждены в отношении меня?",callback_data='ans3')
            	item4 = types.InlineKeyboardButton("В каких случаях судебный исполнитель выставляет запрет на выезд должника за пределы Республики Казахстан?",callback_data='ans4')
            	item5 = types.InlineKeyboardButton("Я оплатил долг по исполнительному производству, но состою в Едином реестре должников, что делать?",callback_data='ans5')
            	item6 = types.InlineKeyboardButton("Назад", callback_data='cancel')

            	markup.add(item1, item2, item3, item4, item5, item6)
            	bot.send_message(call.message.chat.id, 'Выберите нужное из списка', reply_markup=markup)

            elif call.data == 'ans1':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	bot.send_message(call.message.chat.id,'Что делать в случае наложения ареста ЧСИ на Ваши расчетные счета в банках второго уровня?')
            	bot.send_message(call.message.chat.id, 'Ответ: обратиться к ЧСИ наложивший арест, в случае непогашенной задолженности погасить долг и предоставить ЧСИ  подтверждающий документ для последующего снятия ареста.')
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data == 'ans2':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	bot.send_message(call.message.chat.id,'Как и куда можно предъявить исполнительный документ на исполнении к судебному исполнителю?')
            	bot.send_message(call.message.chat.id, 'Ответ: оригинал исполнительного документа  предъявляется к исполнению по месту нахождению должника в Региональную палату частных судебных исполнителей либо к частному судебному исполнителю исполнительного округа по Вашему выбору.')
            	bot.send_message(call.message.chat.id,'Контактные данные частных судебных исполнителей размещены на официальных сайтах Министерства юстиции (www.adilet.gov.kz) и Республиканской палаты частных судебных исполнителей  (www.zhso.kz).')
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data == 'ans3':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	bot.send_message(call.message.chat.id,'Как можно узнать какие исполнительные производства возбуждены в отношении меня?')
            	bot.send_message(call.message.chat.id,'Ответ: для получения информации по исполнительным производствам возбужденных в отношении Вас, можно узнать в Едином реестре должников по ссылке https://aisoip.adilet.gov.kz.')
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data == 'ans4':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	bot.send_message(call.message.chat.id,'В каких случаях судебный исполнитель выставляет запрет на выезд должника за пределы Республики Казахстан?')
            	bot.send_message(call.message.chat.id,'Ответ: по исполнительным производствам, где сумма задолженности превышает 40 месячных расчетных показателей  (МРП).')
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")
            elif call.data == 'ans5':
            	bot.delete_message(call.message.chat.id, call.message.message_id)
            	bot.send_message(call.message.chat.id,'Я оплатил долг по исполнительному производству, но состою в Едином реестре должников, что делать?')
            	bot.send_message(call.message.chat.id,'Ответ: для разрешения данного вопроса необходимо обратиться к судебному исполнителю, либо в Департамент юстиции с подтверждающим документом об оплате долга.')
            	bot.answer_callback_query(call.id, show_alert=True, text="Чтобы вернуть Меню отправьте любое сообщение")



    except Exception as e:
        print(repr(e))
	
	
# RUN
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		test.do("Бот умерац сделал разок")
		print(repr(e))
		time.sleep(5)