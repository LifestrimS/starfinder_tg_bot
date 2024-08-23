import config
import json
import ast
import telebot # pip install telebot
from telebot import types # pip install pyTelegramBotAPI
from character import Character, Skill

bot = telebot.TeleBot(config.token)

#Bot for using Starfinder charactersheet from Myth-Weavers

messageJSON = ''
character = Character
skills = []

savingToJSON = False

@bot.message_handler(commands=['go', 'start']) 
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Upload JSON")
    item2 = types.KeyboardButton("Roll")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Hello there, {0.first_name}!\n\n"
                     "<i>Have a nice time</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    

@bot.message_handler(commands=['endJSON'])
def endWriteJSON(message):
    bot.send_message(message.chat.id, 'End of writing JSON')
    global savingToJSON
    global messageJSON
    savingToJSON = False
    saveJSON(message)

def saveJSON(message):
    global messageJSON
    global character
    global skills

    data = json.loads(messageJSON)

    for i in range(20):
        skillName = data['skill_' + str(i+1) + '_name']
        skillMod = data['skill_' + str(i+1) + '_skill_mod']
        skillAbil = data['skill_' + str(i+1) + '_abil']
        skillAbilMod = data['skill_' + str(i+1) + '_abil_mod']

        skill = Skill(skill_name=skillName, skill_abil=skillAbil, skill_mod=skillMod, skill_abil_mod=skillAbilMod)
        skills.append(skill)
    
    character = Character(skills=skills)
    bot.send_message(message.chat.id, 'Saved!'.format(message.from_user))

def parseIntJson(int):
    return str(int)

@bot.message_handler(content_types=["text"])
def go_send_messages(message):
    print(f'go_send_messages: {message}')
    global savingToJSON
    global messageJSON
    if (savingToJSON):
        messageJSON += message.text

    elif message.chat.type == 'private':
        if message.text == 'Upload JSON':
            savingToJSON = True
            bot.send_message(message.chat.id, 'Enter JSON:')

        elif message.text == "Roll":
            global skills
            one_markup = types.InlineKeyboardMarkup(row_width=2)
            ite0 = types.InlineKeyboardButton(skills[0].skill_name + ' +' + skills[0].skill_mod, callback_data="0")
            ite0_0 = types.InlineKeyboardButton('Shadow roll', callback_data="0_0")

            ite1 = types.InlineKeyboardButton(skills[1].skill_name + ' +' + skills[1].skill_mod, callback_data="1")
            ite1_0 = types.InlineKeyboardButton('Shadow roll', callback_data="1_0")

            ite2 = types.InlineKeyboardButton(skills[2].skill_name + ' +' + skills[2].skill_mod, callback_data="2")
            ite2_0 = types.InlineKeyboardButton('Shadow roll', callback_data="2_0")

            ite3 = types.InlineKeyboardButton(skills[3].skill_name + ' +' + skills[3].skill_mod, callback_data="3")
            ite3_0 = types.InlineKeyboardButton('Shadow roll', callback_data="3_0")

            ite4 = types.InlineKeyboardButton(skills[4].skill_name + ' +' + skills[4].skill_mod, callback_data="4")
            ite4_0 = types.InlineKeyboardButton('Shadow roll', callback_data="4_0")

            ite5 = types.InlineKeyboardButton(skills[5].skill_name + ' +' + skills[5].skill_mod, callback_data="5")
            ite5_0 = types.InlineKeyboardButton('Shadow roll', callback_data="5_0")

            ite6 = types.InlineKeyboardButton(skills[6].skill_name + ' +' + skills[6].skill_mod, callback_data="6")
            ite6_0 = types.InlineKeyboardButton('Shadow roll', callback_data="6_0")

            ite7 = types.InlineKeyboardButton(skills[7].skill_name + ' +' + skills[7].skill_mod, callback_data="7")
            ite7_0 = types.InlineKeyboardButton('Shadow roll', callback_data="7_0")

            ite8 = types.InlineKeyboardButton(skills[8].skill_name + ' +' + skills[8].skill_mod, callback_data="8")
            ite8_0 = types.InlineKeyboardButton('Shadow roll', callback_data="8_0")

            ite9 = types.InlineKeyboardButton(skills[9].skill_name + ' +' + skills[9].skill_mod, callback_data="9")
            ite9_0 = types.InlineKeyboardButton('Shadow roll', callback_data="9_0")

            ite10 = types.InlineKeyboardButton(skills[10].skill_name + ' +' + skills[10].skill_mod, callback_data="10")
            ite10_0 = types.InlineKeyboardButton('Shadow roll', callback_data="10_0")

            ite11 = types.InlineKeyboardButton(skills[11].skill_name + ' +' + skills[11].skill_mod, callback_data="11")
            ite11_0 = types.InlineKeyboardButton('Shadow roll', callback_data="11_0")

            ite12 = types.InlineKeyboardButton(skills[12].skill_name + ' +' + skills[12].skill_mod, callback_data="12")
            ite12_0 = types.InlineKeyboardButton('Shadow roll', callback_data="12_0")

            ite13 = types.InlineKeyboardButton(skills[13].skill_name + ' +' + skills[13].skill_mod, callback_data="13")
            ite13_0 = types.InlineKeyboardButton('Shadow roll', callback_data="13_0")

            ite14 = types.InlineKeyboardButton(skills[14].skill_name + ' +' + skills[14].skill_mod, callback_data="14")
            ite14_0 = types.InlineKeyboardButton('Shadow roll', callback_data="14_0")

            ite15 = types.InlineKeyboardButton(skills[15].skill_name + ' +' + skills[15].skill_mod, callback_data="15")
            ite15_0 = types.InlineKeyboardButton('Shadow roll', callback_data="15_0")

            ite16 = types.InlineKeyboardButton(skills[16].skill_name + ' +' + skills[16].skill_mod, callback_data="16")
            ite16_0 = types.InlineKeyboardButton('Shadow roll', callback_data="16_0")

            ite17 = types.InlineKeyboardButton(skills[17].skill_name + ' +' + skills[17].skill_mod, callback_data="17")
            ite17_0 = types.InlineKeyboardButton('Shadow roll', callback_data="17_0")

            ite18 = types.InlineKeyboardButton(skills[18].skill_name + ' +' + skills[18].skill_mod, callback_data="18")
            ite18_0 = types.InlineKeyboardButton('Shadow roll', callback_data="18_0")

            ite19 = types.InlineKeyboardButton(skills[19].skill_name + ' +' + skills[19].skill_mod, callback_data="19")
            ite19_0 = types.InlineKeyboardButton('Shadow roll', callback_data="19_0")
            one_markup.add(ite0, ite0_0, 
                           ite1, ite1_0,
                           ite2, ite2_0, 
                           ite3, ite3_0, 
                           ite4, ite4_0, 
                           ite5, ite5_0, 
                           ite6, ite6_0, 
                           ite7, ite7_0, 
                           ite8, ite8_0, 
                           ite9, ite9_0, 
                           ite10, ite10_0,
                           ite11, ite11_0,
                           ite12, ite12_0, 
                           ite13, ite13_0, 
                           ite14, ite14_0, 
                           ite15, ite15_0, 
                           ite16, ite16_0, 
                           ite17, ite17_0, 
                           ite18, ite18_0, 
                           ite19, ite19_0,
                           )

            bot.send_message(message.chat.id, "Which skill?".format(
                message.from_user),parse_mode="html", reply_markup=one_markup)
            
@bot.callback_query_handler(func=lambda call: call.data in ['0', '0_0', 
                                                            '1', '1_0', 
                                                            '2', '2_0', 
                                                            '3', '3_0', 
                                                            '4', '4_0', 
                                                            '5', '5_0', 
                                                            '6', '6_0', 
                                                            '7', '7_0', 
                                                            '8', '8_0', 
                                                            '9', '9_0', 
                                                            '10', '10_0', 
                                                            '11', '11_0', 
                                                            '12', '12_0', 
                                                            '13', '13_0', 
                                                            '14', '14_0', 
                                                            '15', '15_0', 
                                                            '16', '16_0', 
                                                            '17', '17_0',
                                                            '18', '18_0',
                                                            '19', '19_0',]) 
def callback_inline_one(call):
        global character
        bot.answer_callback_query(call.id)
        
        if '_' not in call.data:
            bot.send_message(call.message.chat.id, str(character.skills[int(call.data)].rollString()), parse_mode="html")
        else:
            endOfNumber = call.data.find('_')
            bot.send_message(call.message.chat.id, str(character.skills[int(call.data[:endOfNumber])].shadowRollString()), parse_mode="html")         


@bot.message_handler(commands=['stop'])  # Обработка команды для выхода
def bye(message):

    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Bye, {0.first_name}!\n".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=hideBoard)
    exit()
    
# RUN
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Connection error: ', e)
    except Exception as r:
        print("Exception: ", r)
    finally:
        print("The end of the bot's work")



