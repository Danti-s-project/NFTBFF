from dotenv import load_dotenv
import hmac, hashlib
import os


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def check_hash(data: dict):
    """
    Telegram отправляет в миниапп initData, в котором есть информация о пользователе, а так же ее хеш
    Чтобы убедиться что информация не подделана, вычислим хеш информации по токену бота, и сравним с хешем телеграмма
    Если хеши не совпали, информация подделана

    :param data: initData с фронтенда приложения
    :return: True, если данные правильные, иначе False
    """

    # Выкидываем хеш от телеграмма
    hash_from_telegram = data.pop("hash", None)

    # Крафтим строку которую будем хешировать
    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))

    # Создаем ключ по которому будем хешировать данные
    secret_key = hmac.new(
        key=b"WebAppData", msg=BOT_TOKEN.encode(), digestmod=hashlib.sha256
    ).digest()

    # Считаем хеш
    calculated_hash = hmac.new(
        key=secret_key, msg=data_check_string.encode(), digestmod=hashlib.sha256
    ).hexdigest()

    # Сравниваем
    return calculated_hash == hash_from_telegram
