import requests
from bs4 import BeautifulSoup
import telebot
import time

TOKEN = open('token.txt').readline().strip()
bot = telebot.TeleBot(f'{TOKEN}')
Pogoda = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%D0%B5&oq=&aqs=chrome.2.69i57j69i59l2j0i10i131i433i512l3j0i131i433l4.2504j0j7&sourceid=chrome&ie=UTF-8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в приложение\n*"MEGA POGODA"!*\nнапишите команду "/pogoda" чтобы узнать погоду', parse_mode='Markdown')

@bot.message_handler(commands=['pogoda'])
def show(message):
    full_page = requests.get(Pogoda, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_temp = soup.findAll("span", {"class": "wob_t q8U8x", "id": "wob_tm", "style": "display:inline"})
    full_page = requests.get(Pogoda, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_precipitation = soup.findAll("span", {"id": "wob_pp"})
    full_page = requests.get(Pogoda, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_humidity = soup.findAll("span", {"id": "wob_hm"})
    full_page = requests.get(Pogoda, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_wind = soup.findAll("span", {"class": "wob_t", "id": "wob_ws"})
    bot.send_message(message.chat.id, 'Температура: ' + convert_temp[0].text + '°C' + '\n' + 'Вероятность осадков: ' + convert_precipitation[0].text + '\n' + 'Влажность: ' + convert_humidity[0].text + '\n' + 'Ветер: ' + convert_wind[0].text ,parse_mode='Markdown')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)