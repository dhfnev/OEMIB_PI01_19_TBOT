import os
import requests
import telebot

def get_random_anime(message):
    response = requests.post(url='http://api.jikan.moe/v4/random/anime')
    r = response.json().get("data")

    anime_name = r.get("title")
    anime_episodes = r.get("episodes")
    anime_type = r.get("type")
    anime_year = r.get("year")
    anime_synopsis = r.get("synopsis")
    anime_images = r.get("images").get("jpg").get("image_url")

    if anime_episodes is None:
        anime_episodes = "число эпизодов не известно"
    else:
        anime_episodes = anime_episodes

    if anime_year is None:
        anime_year = "неизвестного года выпуска"
    else:
        anime_year = anime_year

    if anime_synopsis is None:
        anime_synopsis = "отсутствует"
    else:
        anime_synopsis = anime_synopsis

    if anime_images is None:
        bot.send_message(message.chat.id,text=f"Название: {anime_name}. \nКол-во эпизодов: {anime_episodes}. \nФормат: {anime_type}.\nГод выпуска: {anime_year}.\nКраткое описание: {anime_synopsis}")
    else:
        bot.send_photo(message.chat.id,caption=f"Название: {anime_name}. \nКол-во эпизодов: {anime_episodes}. \nФормат: {anime_type}.\nГод выпуска: {anime_year}.\nКраткое описание: {anime_synopsis}", photo=anime_images)

def get_random_anime(message):
    response = requests.post(url='http://api.jikan.moe/v4/random/manga')
    r = response.json().get("data")

    manga_name = r.get("title")
    manga_chapters = r.get("chapters")
    manga_volumes = r.get("volumes")
    manga_status = r.get("status")
    manga_popularity = r.get("popularity")
    manga_synopsis =r.get("synopsis")
    manga_images = r.get("images").get("jpg").get("image_url")

    if manga_volumes == None:
        manga_volumes = 1
    else:
        manga_volumes = manga_volumes

    if manga_synopsis == None:
        manga_synopsis = "отсутствует"
    else:
        manga_synopsis = manga_synopsis

    if manga_status == "Finished":
        manga_status = "Завершена"
    else:
        manga_status = "Издается"

    if manga_status == "Завершена":
        message_text = f"Название: {manga_name}.\nКол-во глав: {manga_chapters}.\nКол-во томов: {manga_volumes}.\nСтатус: {manga_status}.\nКраткое описание: {manga_synopsis}"
    else:
        message_text = f"Название: {manga_name}.\nОчки популярности:{manga_popularity}\nСтатус: {manga_status}.\nКраткое описание: {manga_synopsis}"

    bot.send_photo(message.chat.id,caption=message_text, photo=manga_images)
