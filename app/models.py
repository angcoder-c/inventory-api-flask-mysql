import datetime
from . import db
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, Numeric, func
from sqlalchemy.orm import relationship


class Category(db.Model):
    
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    products = relationship('Product', backref='category'),

class Product(db.Model):
    
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())

class Store(db.Model):
    
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(Text, nullable=False)
    orders = relationship('Order', backref='store')

class User(db.Model):
    
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(Text)
    phone = Column(String(20), nullable=False)
    role = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
    orders = relationship('Order', backref='user')

class Provider(db.Model):
    
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(50))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
    products = relationship('Product', secondary='product_provider', backref='providers')

class ProductProvider(db.Model):
    
    __tablename__ = 'product_provider'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    provider_id = Column(Integer, ForeignKey('providers.id'), primary_key=True)

class Order(db.Model):
    
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'))
    store_id = Column(Integer, db.ForeignKey('stores.id'))
    total = Column(Numeric(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
    items = relationship('OrderItem', backref='order')

class OrderItem(db.Model):
    
    __tablename__ = 'order_items'
    
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    product = relationship('Product')

    