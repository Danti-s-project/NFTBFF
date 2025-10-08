import os

import aiohttp

from models import UserInfo


async def get_user_info(user_id: int) -> UserInfo | None:
    """
    Получить информацию о пользователе по userid

    :param user_id: telegram user_id
    :return: UserInfo Model
    """
    user_info = {}

    async with aiohttp.ClientSession() as session:
        # Получаем основную информацию о пользователе
        async with session.get(f'{os.getenv("BACKEND_HOST")}/api/v1/users/{user_id}/') as response:
            # Если пользователя не существует, возвращаем None
            if response.status == 404:
                return None

            user_info += await response.json()

        # Получаем информацию о курсах
        async with session.get(f'{os.getenv("BACKEND_HOST")}/api/v1/p2p_course/?user_id={user_id}') as response:
            user_info += {"p2p_course_lessons_completed": len(await response.json())}
        async with session.get(f'{os.getenv("BACKEND_HOST")}/api/v1/toncoin_course/?user_id={user_id}') as response:
            user_info += {"toncoin_course_lessons_completed": len(await response.json())}
        async with session.get(f'{os.getenv("BACKEND_HOST")}/api/v1/scam_course/?user_id={user_id}') as response:
            user_info += {"scam_course_lessons_completed": len(await response.json())}
        async with session.get(f'{os.getenv("BACKEND_HOST")}/api/v1/nft_sell_course/?user_id={user_id}') as response:
            user_info += {"nft_sell_course_lessons_completed": len(await response.json())}

    return UserInfo(**user_info)
