from pydantic import BaseModel
from datetime import datetime


class UserInfo(BaseModel):
    """
    Telegram-id пользователя
    """
    user_id: int

    """
    Telegram username пользователя. Может быть None.
    """
    username: str = None

    """
    Фамилия + Имя пользователя в телеграмм
    """
    fullname: str

    """
    Дата регистрации
    """
    registration_date: datetime

    """
    Код языка (ru, en, zh)
    """
    language: str

    """
    Если True, пользователь является премиум подписчиком, иначе False.
    """
    is_premium: bool

    """
    Баланс пользователя в местной валюте
    """
    balance: float

    """
    Количество завершенных уроков в Ton coin курсе
    """
    toncoin_course_lessons_completed: int

    """
    Количество завершенных уроков в nft-sell курсе
    """
    nft_sell_course_lessons_completed: int

    """
    Количество завершенных уроков в p2p курсе
    """
    p2p_course_lessons_completed: int

    """
    Количество завершенных уроков в скам курсе
    """
    scam_course_lessons_completed: int
