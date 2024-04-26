'''
requests live here
'''

from sqlalchemy import select

from app.db.models import async_session
from app.db.models import Category, Item, User


async def set_user(tg_id):
    '''
    добавление юзера при отсутствии в бд
    '''
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()
