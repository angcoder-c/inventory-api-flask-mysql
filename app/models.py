import datetime
from . import db
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, Numeric, func
from sqlalchemy.orm import relationship

class Product(db.Model):
    
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())

    @staticmethod
    def to_dict(product):
        return {
            'id' : product.id,
            'name' : product.name,
            'description' : product.description,
            'price' : product.price,
            'quantity' : product.quantity,
            'category_id' : product.category_id,
            'created_at' : product.created_at,
        }

class Category(db.Model):
    
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    products = relationship('Product', backref='category')

    @staticmethod
    def to_dict(category):
        return {
            'id' : category.id,
            'name' : category.name,
            'description' : category.description,
            'products' : [
                Product.to_dict(product) 
                for product 
                in category.products
            ]
        }


class Store(db.Model):
    
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(Text, nullable=False)
    orders = relationship('Order', backref='store')

    @staticmethod
    def to_dict(store):
        return {
            'id' : store.id,
            'name' : store.name,
            'address' : store.address,
            'orders' : [
                Order.to_dict(order) 
                for order 
                in store.orders
            ]
        }

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

    @staticmethod
    def to_dict(user):
        return {
            'id' : user.id,
            'name' : user.name,
            'address' : user.address,
            'role' : user.role,
            'password' : user.password,
            'created_at' : user.created_at,
            'orders' : [
                Order.to_dict(order) 
                for order 
                in user.orders
            ]
        }

class Provider(db.Model):
    
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(50))
    created_at = Column(TIMESTAMP, default=func.current_timestamp())
    products = relationship('Product', secondary='product_provider', backref='providers')

    @staticmethod
    def to_dict(provider):
        return {
            'id' : provider.id,
            'name' : provider.name,
            'phone' : provider.phone,
            'created_at' : provider.created_at,
            'products' : [
                Product.to_dict(product) 
                for product 
                in provider.products
            ]
        }

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

    @staticmethod
    def to_dict(order):
        return {
            'id': order.id,
            'user_id': order.user_id,
            'store_id': order.store_id,
            'total': order.total,
            'created_at': order.created_at,
            'items': [
                OrderItem.to_dict(item) 
                for item 
                in order.items
            ]
        }

class OrderItem(db.Model):
    
    __tablename__ = 'order_items'
    
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    product = relationship('Product')

    @staticmethod
    def to_dict(order_item):
        return {
            'order_id': order_item.order_id,
            'product_id': order_item.product_id,
            'quantity': order_item.quantity,
            'price': order_item.price,
            'product': Product.to_dict(order_item.product) if order_item.product else None
        }