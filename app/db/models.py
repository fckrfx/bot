'''
models live here
'''

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (AsyncAttrs,
                                    async_sessionmaker,
                                    create_async_engine,
                                    )


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    '''
    общий класс БД
    '''
    pass


class User(Base):
    '''
    класс пользователей
    '''
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    phone: Mapped[int] = mapped_column()


class Category(Base):
    '''
    класс категорий
    '''
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))


class Item(Base):
    '''
    класс объектов
    '''
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    description: Mapped[str] = mapped_column(String(120))
    price: Mapped[int] = mapped_column()


async def async_main():
    '''
    создаватель бд
    '''
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
