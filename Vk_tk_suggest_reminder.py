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
from_hu_kirovohrad = "-78300063"
from_hello_now = "-77586277"
from_kirovohrad_instagram = "-46259225"

tk_suggested_posts = vkapi('wall.get', owner_id=from_typical_kirovohrad, filter='suggests', count=100)
tk_today_posts = vkapi('wall.get', owner_id=from_typical_kirovohrad, filter='all', count=100)
tk_today_posts_poned = vkapi('wall.get', owner_id=from_typical_kirovohrad, filter='postponed', count=100)
scandal_kirovohrad = vkapi('wall.get', owner_id=from_scandal_kirovohrad, filter='suggests', count=100)
hu_kirovohrad = vkapi('wall.get', owner_id=from_hu_kirovohrad, filter = 'suggests', count=100)
hello_now = vkapi('wall.get', owner_id=from_hello_now, filter='suggests', count=100)
kirovohrad_instagram = vkapi('wall.get', owner_id=from_kirovohrad_instagram, filter='suggests', count=100)

tk_suggested_posts = tk_suggested_posts['count']
tk_today_posts_list = tk_today_posts['items']
tk_today_posts_poned_list = tk_today_posts_poned['items']
scandal_kirovohrad = scandal_kirovohrad['count']
hu_kirovohrad = hu_kirovohrad['count']
hello_now = hello_now['count']
kirovohrad_instagram = kirovohrad_instagram['count']

post_list = []
postponed_list = []
for post in tk_today_posts_list:
    post_date = post['date']
    post_date_human = datetime.datetime.fromtimestamp(post_date).strftime('%Y-%m-%d')
    if post_date_human == curr_date:
        post_list.append(post_date_human)
if tk_today_posts_poned_list:
    for postponed in tk_today_posts_poned_list:
        post_date = postponed['date']
        post_date_human = datetime.datetime.fromtimestamp(post_date).strftime('%Y-%m-%d')
        if post_date_human == curr_date:
            post_list.append(post_date_human)
            postponed_list.append(post_date_human)

# Working groups
supreme_court_tk = "-48030958"
# print(post_list)
# print(len(post_list))

if tk_suggested_posts:
    sleep(1)
    wall_post = vkapi('wall.post',
                      owner_id=supreme_court_tk,
                      from_group='1',
                      message="&#9888; В собществе: @typical_kirovohrad обнаружены предложенные посты:\n\n"
                              "&#9889; Количество: "+str(tk_suggested_posts)+"\n"
                              "&#10071; Всего на стене: "+str(len(post_list))+", из них отложка: "+str(len(postponed_list))+" \ Max 50\n\n"
                              "Администраторы, пожалуйста разберите предложку!\n"
                              "@elitenigga \n"
                              "@1dinozavrik1 \n"
                              "@id5766876 \n"
                              "@ich_bin_deine_sonne \n"
                              "@kyzzzenka \n"
                              "@mcklad \n",
                      signed='0')
    print("There are some post found in typical_kirovohrad - post sent!" + str(tk_suggested_posts))
else:
    print("There are no suggested posts in typical_kirovohrad!")

if scandal_kirovohrad:
    sleep(2)
    wall_post = vkapi('wall.post',
                      owner_id=supreme_court_tk,
                      from_group='1',
                      message="В собществе: @scandal_kir обнаружены предложенные посты\n\n"
                              "Количество: " + str(scandal_kirovohrad) + "\n\n"
                              "Администраторы, пожалуйста разберите предложку!\n"
                              "@id84247513 \n"
                              "@kyzzzenka \n",
                      signed='0')
    print("There are some post found in scandal_kirovohrad - post sent!" + str(scandal_kirovohrad))
else:
    print("There are no suggested posts in scandal_kirovohrad!")

if hello_now:
    sleep(3)
    wall_post = vkapi('wall.post',
                      owner_id=supreme_court_tk,
                      from_group='1',
                      message="В собществе: @now_tk обнаружены предложенные посты\n\n"
                              "Количество: " + str(hello_now) + "\n\n"
                              "Администраторы, пожалуйста разберите предложку!\n"
                              "@elitenigga \n"
                              "@crucian__i \n"
                              "@mcklad \n"
                              "@sanyaaa_klim \n",
                      signed='0')
    print("There are some post found in hello_now - post sent!" + str(hello_now))
else:
    print("There are no suggested posts in hello_now!")

if kirovohrad_instagram:
    sleep(4)
    wall_post = vkapi('wall.post',
                      owner_id=supreme_court_tk,
                      from_group='1',
                      message="В собществе: @kir_instagram обнаружены предложенные посты\n\n"
                              "Количество: " + str(kirovohrad_instagram) + "\n\n"
                              "Администраторы, пожалуйста разберите предложку!\n"
                              "@elitenigga \n"
                              "@ich_bin_deine_sonne \n",
                      signed='0')
    print("There are some post found in kirovohrad_instagram - post sent!" + str(kirovohrad_instagram))
else:
    print("There are no suggested posts in kirovohrad_instagram!")

if hu_kirovohrad:
    sleep(5)
    wall_post = vkapi('wall.post',
                      owner_id=supreme_court_tk,
                      from_group='1',
                      message="В собществе: @hu_kirovohrad обнаружены предложенные посты\n\n"
                              "Количество: " + str(hu_kirovohrad) + "\n\n"
                              "Администраторы, пожалуйста разберите предложку!\n"
                              "@id5766876 \n"
                              "@id59914493 \n"
                              "@misuri1337 \n",
                      signed='0')
    print("There are some post found in hu_kirovohrad - post sent!" + str(hu_kirovohrad))
else:
    print("There are no suggested posts in hu_kirovohrad!")