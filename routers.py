from urllib.parse import parse_qsl

from dotenv import load_dotenv
from fastapi import Request, HTTPException

from app import app
from models import UserInfo
from check_hash import check_hash
from service import get_user_info

load_dotenv()
BASE_URL = '/api/v1'


@app.post(BASE_URL + '/user_info/', response_model=UserInfo)
async def get_user_info(request: Request):
    """
    Получите информацию о пользователе

    :param request: fastapi request
    :return: 403 если данные невалидны, 404 если пользователя не существует, иначе UserInfo
    """

    body = await request.json()
    init_data = dict(parse_qsl(body.get('initData'), strict_parsing=True))

    if not check_hash(init_data):
        return HTTPException(status_code=403, detail="Unauthorized")


    user_info = await get_user_info(init_data['id'])

    if not user_info:
        return HTTPException(status_code=404, detail="User not found")
    return user_info
