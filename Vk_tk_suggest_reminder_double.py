#! /usr/bin/env python3
# coding=utf-8
__author__ = 'danilcha'

import vk
from time import sleep, strftime, gmtime
import datetime

# TODO:
# New version for Vkontakte api for module ver 2.0a4 and above
token = '3f18130f132411eebb3bfbdc113fc00693a09a98626e2703aea2c04b91cebad5088e2466d590d95760674'
# session = vk.Session(access_token=token)
vkapi = vk.API(access_token = token)
# vkapi = vk.API(session)

curr_date = strftime("%Y-%m-%d")

from_typical_kirovohrad = "-46631810"
from_scandal_kirovohrad = "-80849532"
from_hello_now = "-77586277"
from_kirovohrad_instagram = "-46259225"
from_hu_kirovohrad = "-78300063"

tk_suggested_posts = vkapi('wall.get', owner_id=from_typical_kirovohrad, filter='suggests', count=100)
tk_today_posts = vkapi('wall.get', owner_id=from_typical_kirovohrad, filter='all', count=100)
tk_today_posts_poned = vkapi('wall.get', owner_id=from_typical_kirovohrad, filter='postponed', count=100)
scandal_kirovohrad = vkapi('wall.get', owner_id=from_scandal_kirovohrad, filter='suggests', count=100)
hello_now = vkapi('wall.get', owner_id=from_hello_now, filter='suggests', count=100)
kirovohrad_instagram = vkapi('wall.get', owner_id=from_kirovohrad_instagram, filter='suggests', count=100)
hu_kirovohrad = vkapi('wall.get', owner_id=from_hu_kirovohrad, filter = 'suggests', count=100)


tk_suggested_posts_cnt = tk_suggested_posts['count']
tk_today_posts_list_cnt = tk_today_posts['items']
tk_today_posts_poned_list_cnt = tk_today_posts_poned['items']
scandal_kirovohrad_cnt = scandal_kirovohrad['count']
hello_now_cnt = hello_now['count']
hu_kirovohrad_cnt = hu_kirovohrad['count']
kirovohrad_instagram_cnt = kirovohrad_instagram['count']

post_list = []
postponed_list = []
for post in tk_today_posts_list_cnt:
    post_date = post['date']
    post_date_human = datetime.datetime.fromtimestamp(post_date).strftime('%Y-%m-%d')
    if post_date_human == curr_date:
        post_list.append(post_date_human)
if tk_today_posts_poned_list_cnt:
    for postponed in tk_today_posts_poned_list_cnt:
        post_date = postponed['date']
        post_date_human = datetime.datetime.fromtimestamp(post_date).strftime('%Y-%m-%d')
        if post_date_human == curr_date:
            post_list.append(post_date_human)
            postponed_list.append(post_date_human)

def SuggestedPostsList(items, public_id):
    suggested_list = []
    suggested_posts_items = items['items']
    if suggested_posts_items:
        for suggested_post in suggested_posts_items:
            post_id = suggested_post['id']
            post_item = "https://vk.com/wall"+public_id+"_"+str(post_id)+" \n"
            suggested_list.append(post_item)
    else:
        print("No suggested posts found")
    suggested_sting = ''.join(suggested_list)
    return suggested_sting

# Working groups and options
supreme_court_tk = "-48030958"
bot_chat = 92
post_option = 1
message_option = 1

if tk_suggested_posts_cnt:
    suggested_sting = SuggestedPostsList(tk_suggested_posts,from_typical_kirovohrad)
    sleep(1)
    if message_option == 1:
        message = vkapi('messages.send',
                          chat_id=bot_chat,
                          message="&#8505; "
                                  "[Типичный Кировоград] обнаружены предложенные посты:\n"
                                  "&#9889; Количество: "+str(tk_suggested_posts_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+
                                  "\n\n"+'&#8601;'*15+"\n&#128282;"
                          )
        sleep(1)
    else:
        print("Message send option for tk_suggested_posts is in the false state!")
    if post_option == 1:
        wall_post = vkapi('wall.post',
                          owner_id=supreme_court_tk,
                          from_group='1',
                          message="&#9888; "
                                  "В собществе: @typical_kirovohrad обнаружены предложенные посты:\n\n"
                                  "&#9889; Количество: "+str(tk_suggested_posts_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+"\n\n"
                                  "Администраторы, пожалуйста разберите предложку!\n"
                                  "@ich_bin_deine_sonne, @kyzzzenka, @typical_kirovohrad_boss ",
                          signed='0')
        print("There are some post found in typical_kirovohrad - post sent!" + str(tk_suggested_posts_cnt))
    else:
        print("Wall Post option for tk_suggested_posts is in the false state!")
else:
    print("There are no suggested posts in typical_kirovohrad!")

if scandal_kirovohrad_cnt:
    suggested_sting = SuggestedPostsList(scandal_kirovohrad,from_scandal_kirovohrad)
    sleep(2)
    if message_option == 1:
        message = vkapi('messages.send',
                          chat_id=bot_chat,
                          message="&#8505; "
                                  "[СК] Скандал Кировоград] обнаружены предложенные посты\n\n"
                                  "Количество: " + str(scandal_kirovohrad_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+
                                  "\n\n"+'&#8601;'*15+"\n&#128282;"
                          )
        sleep(1)
    else:
        print("Message send option for scandal_kirovohrad is in the false state!")
    if post_option == 1:
        wall_post = vkapi('wall.post',
                          owner_id=supreme_court_tk,
                          from_group='1',
                          message="&#8505; "
                                  "В собществе: @scandal_kir обнаружены предложенные посты\n\n"
                                  "&#9889; Количество: "+str(scandal_kirovohrad_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+"\n\n"
                                  "Администраторы, пожалуйста разберите предложку!\n"
                                  "@kyzzzenka, @ich_bin_deine_sonne, @id217407103",
                          signed='0')
        print("There are some post found in scandal_kirovohrad - post sent!" + str(scandal_kirovohrad_cnt))
    else:
        print("Wall Post option for scandal_kirovohrad is in the false state!")
else:
    print("There are no suggested posts in scandal_kirovohrad!")

if hello_now_cnt:
    suggested_sting = SuggestedPostsList(hello_now,from_hello_now)
    sleep(3)
    if message_option == 1:
        message = vkapi('messages.send',
                          chat_id=bot_chat,
                          message="&#8505; \n"
                                  "[ПК] Привет, сейчас... | Кировоград] обнаружены предложенные посты\n\n"
                                  "&#9889; Количество: "+str(hello_now_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+
                                  "\n\n"+'&#8601;'*15+"\n&#128282;"
                          )
        sleep(2)
    else:
        print("Message send option for hello_now is in the false state!")
    if post_option == 1:
        wall_post = vkapi('wall.post',
                          owner_id=supreme_court_tk,
                          from_group='1',
                          message="&#8505; "
                                  "В собществе: @now_tk обнаружены предложенные посты\n\n"
                                  "&#9889; Количество: "+str(hello_now_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+"\n\n"
                                  "Администраторы, пожалуйста разберите предложку!\n"
                                  "@crucian__i, ",
                          signed='0')
        print("There are some post found in hello_now - post sent!" + str(hello_now_cnt))
    else:
        print("Wall Post option for hello_now is in the false state!")
else:
    print("There are no suggested posts in hello_now!")

if kirovohrad_instagram_cnt:
    suggested_sting = SuggestedPostsList(kirovohrad_instagram,from_kirovohrad_instagram)
    sleep(4)
    if message_option == 1:
        message = vkapi('messages.send',
                          chat_id=bot_chat,
                          message="&#8505; "
                                  "[kirovohrad instagram] обнаружены предложенные посты\n\n"
                                  "&#9889; Количество: "+str(kirovohrad_instagram_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+
                                  "\n\n"+'&#8601;'*15+"\n&#128282;"
                          )
        sleep(2)
    else:
        print("Message send option for kirovohrad_instagram is in the false state!")
    if post_option == 1:
        wall_post = vkapi('wall.post',
                          owner_id=supreme_court_tk,
                          from_group='1',
                          message="&#8505; "
                                  "В собществе: @kir_instagram обнаружены предложенные посты\n\n"
                                  "&#9889; Количество: "+str(kirovohrad_instagram_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+"\n\n"
                                  "Администраторы, пожалуйста разберите предложку!\n"
                                  "@ich_bin_deine_sonne ",
                          signed='0')
        print("There are some post found in kirovohrad_instagram - post sent!" + str(kirovohrad_instagram_cnt))
    else:
        print("Wall Post option for kirovohrad_instagram is in the false state!")
else:
    print("There are no suggested posts in kirovohrad_instagram!")

if hu_kirovohrad_cnt:
    suggested_sting = SuggestedPostsList(hu_kirovohrad,from_hu_kirovohrad)
    sleep(5)
    if message_option == 1:
        message = vkapi('messages.send',
                          chat_id=bot_chat,
                          message="&#8505; "
                                  "[ХК] Хуевый Кировоград] обнаружены предложенные посты\n\n"
                                  "&#9889; Количество: "+str(hu_kirovohrad_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+
                                  "\n\n"+'&#8601;'*15+"\n&#128282;"
                          )
        sleep(2)
    else:
        print("Message send option for hu_kirovohrad is in the false state!")
    if post_option == 1:
        wall_post = vkapi('wall.post',
                          owner_id=supreme_court_tk,
                          from_group='1',
                          message="&#8505; "
                                  "В собществе: @hu_kirovohrad обнаружены предложенные посты\n\n"
                                  "&#9889; Количество: "+str(hu_kirovohrad_cnt)+"\n\n"
                                  "Посты:\n"
                                  +suggested_sting+"\n\n"
                                  "Администраторы, пожалуйста разберите предложку!\n"
                                  "@id5766876, @id59914493, @ich_bin_deine_sonne, @kyzzzenka,"
                          ,
                          signed='0')
        print("There are some post found in hu_kirovohrad - post sent!" + str(hu_kirovohrad_cnt))
    else:
        print("Wall Post option for hu_kirovohrad is in the false state!")
else:
    print("There are no suggested posts in hu_kirovohrad!")

curr_time = strftime("%H:%M")
print(curr_time)

if len(post_list) > 40 and curr_time < '21:00':
    sleep(1)
    # print("work")
    if message_option == 1:
        message = vkapi('messages.send',
                          chat_id=bot_chat,
                          message='&#9888;'*15+"\n"
                                  "ВНИМАНИЕ! На стене сообщества Типичный Кировоград уже более 40 постов!\n"
                                  "&#9654; На стене: ............ "+str(len(post_list))+" \n"
                                  "&#9199; Отложка: ............ "+str(len(postponed_list))+"  \n"
                                  "&#128314; Максимум: .......... 50 \n\n"
                                  "&#128680; Если это предупреждение вышло раньше 21-00 - обратите вниманеие на очередь, "
                                  "чтобы не достигнуть лимита постов раньше.\n"
                                  "\n\n"+'&#8601;'*15+"\n&#128282;"
                          )
        sleep(2)
    else:
        print("Message send option for regular TK counts is in the false state!")
    if post_option == 1:
        wall_post = vkapi('wall.post',
                          owner_id=supreme_court_tk,
                          from_group='1',
                          message='&#9888;'*15+"\n"
                                  "ВНИМАНИЕ! На стене сообщества Типичный Кировоград уже более 40 постов!\n"
                                  "&#9654; На стене: ............ "+str(len(post_list))+" \n"
                                  "&#9199; Отложка: ............ "+str(len(postponed_list))+"  \n"
                                  "&#128314; Максимум: .......... 50 \n\n"
                                  "&#128680; Если это предупреждение вышло раньше 21-00 - обратите вниманеие на очередь, "
                                  "чтобы не достигнуть лимита постов раньше.\n"
                                  "@id5766876, @ich_bin_deine_sonne, @kyzzzenka, @typical_kirovohrad_boss "
                                  "&#128282;",
                          signed='0')
        print("There are more than 40 posts on wall - post sent!" +str(len(post_list)))
    else:
        print("Wall Post option for regular TK counts is in the false state!")
else:
    if message_option == 1:
        sleep(5)
        message = vkapi('messages.send',
                          chat_id=bot_chat,
                          message="&#8505; \n"
                                  "&#9654; На стене: ............ "+str(len(post_list))+" \n"
                                  "&#9199; Отложка: ............ "+str(len(postponed_list))+"  \n"
                                  "&#128314; Максимум: .......... 50 \n\n"
                                  "Регулярный счетчик постов в паблике ""Типичный Кировоград"" \n"
                                  "Старайтесь заполнить стену так, чтобы к концу дня "
                                  "на ней было максимальное кол-во постов, можно вручную.\n"
                                  "\n\n"+'&#8601;'*15+"\n&#128282;"
                          )
        print("Regular reminder of post count: "+str(len(post_list)))
    else:
        print("Message send option for regular TK counts is in the false state!")