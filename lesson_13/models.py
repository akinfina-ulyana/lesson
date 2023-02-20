from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base  # для объявления таблиц в декларативном массиве
from sqlalchemy.orm import relationship  # возможно связывает объекты

Base = declarative_base() # все классы, которые будут описывать таблицы существующие или будущие будут наследоваться от
                          # данного экземпляра класса

class User(Base):
    __tablename__ = "user"    # имя таблицы с которой связывается данный экземпляр класса
    # (либо таблица будет создаваться если её нет в бд)
    id = Column(Integer, primary_key=True)  # столбец со значением инт и устанавливается что это первичный ключ
    email = Column(String)
    password = Column(String)

    profile = relationship("Profile", back_populates="user", uselist=False)
    addresses = relationship("Address", back_populates="user")
    purchases = relationship("Purchase", back_populates="user")


class Profile(Base):
    __tablename__ = "profile"m
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    age = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id")) # являетсяс внешним ключом по отношению в стобцу id таблицы user
    user = relationship("User", back_populates="profile", uselist=False)


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    address = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="addresses", uselist=False)


class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    product_id = Column(ForeignKey("product.id"), primary_key=True)
    count = Column(Integer)

    user = relationship("User", back_populates="purchases", uselist=False)
    product = relationship("Product", back_populates="purchases", uselist=False)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    purchases = relationship("Purchase", back_populates="product")