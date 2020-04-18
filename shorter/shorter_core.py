from random import choice
import string
from . import models

HOST = '127.0.0.1:8000' # Перенаправляющий сайт

def to_short(longurl):

    try:
        # Если адрес существует, то возвращаем короткую ссылку из базы
        return models.Main_db.objects.get(longurl=longurl).shorturl
    except(Exception):
        shorturl = HOST + '/' +''.join(choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(5))
        add_to_base(shorturl, longurl)
        return shorturl

def add_to_base(short_url, long_url):
    try:
        # Если кароткий адрес существует, то создаем новый
        if not check(long_url):
            long_url = 'http://' + long_url
        models.Main_db.objects.get(shorturl=short_url)
        to_short(long_url)
    except(models.Main_db.DoesNotExist):
        # Если адрес начинается с "https://" или "http://", то добавляем в базу неизмененный вариант
        # Иначе добавляем к адресу приставку "http://"
        models.Main_db.objects.create(shorturl=short_url, longurl=check(long_url))

# Получение из базы адреса по его короткому варианту
def get_longurl(short_url):
    return models.Main_db.objects.get(shorturl=short_url).longurl

def del_from_base(id):
    models.Main_db.objects.get(id=id).delete()

# Проверка наличия в адресе "https://" или "http://"
def check(sitename):
    tmp1 = '' # https://
    tmp2 = '' # http://

    if len(sitename) < 8:
        return 'http://' + sitename

    i = 0
    while i < 8:
        tmp1 += sitename[i]
        if i < 7:
            tmp2 += sitename[i]
        i += 1

    if tmp1 == 'https://' or tmp2 == 'http://':
        return sitename

    return 'http://' + sitename
