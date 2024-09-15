CREATE DATABASE IF NOT EXISTS inventory_db;

USE inventory_db;

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS stores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    phone VARCHAR(20) NOT NULL,
    role VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS providers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_provider (
    product_id INT,
    provider_id INT,
    PRIMARY KEY (product_id, provider_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (provider_id) REFERENCES providers(id)
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    store_id INT,
    total DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (store_id) REFERENCES stores(id)
);

CREATE TABLE IF NOT EXISTS order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO categories (name, description) VALUES
('Electrónica', 'Dispositivos electrónicos y gadgets'),
('Ropa', 'Prendas de vestir y accesorios'),
('Alimentos', 'Productos alimenticios y bebidas');

INSERT INTO products (name, description, price, quantity, category_id) VALUES
('Teléfono inteligente', 'Teléfono con pantalla táctil y cámara avanzada', 799.99, 50, 1),
('Laptop', 'Portátil con 16GB RAM y SSD de 512GB', 1200.00, 20, 1),
('Camiseta', 'Camiseta de algodón 100% para hombre', 19.99, 100, 2),
('Pantalón de mezclilla', 'Jeans para mujer con diseño ajustado', 49.99, 60, 2),
('Cereal de avena', 'Cereal saludable de avena y frutas', 3.99, 200, 3),
('Galletas de chocolate', 'Galletas crujientes con chips de chocolate', 2.99, 150, 3);

INSERT INTO stores (name, address) VALUES
('Tienda Central', 'Av. Principal 123, Ciudad Central'),
('Sucursal Norte', 'Calle Norte 456, Ciudad Norte'),
('Sucursal Sur', 'Calle Sur 789, Ciudad Sur');

INSERT INTO users (name, address, phone, role, email, password) VALUES
('ADMIN', 'ADMIN', 'ADMIN', 'ADMIN', 'admin@admin.com', 'password'),
('Juan Pérez', 'Calle Falsa 123, Ciudad Falsa', '5555-1234', 'CLIENT', 'jp@example.com', 'password'),
('María González', 'Calle Real 456, Ciudad Real', '5555-5678', 'CLIENT', 'mg@example.com', 'password'),
('Pedro Ramírez', 'Av. Siempre Viva 789, Springfield', '5555-9101', 'CLIENT', 'pr@example.com', 'password');

INSERT INTO providers (name, phone) VALUES
('Proveedor Electrónica', '5555-2020'),
('Proveedor Ropa', '5555-3030'),
('Proveedor Alimentos', '5555-4040');

INSERT INTO product_provider (product_id, provider_id) VALUES
(1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3);

INSERT INTO orders (user_id, store_id, total) VALUES
(2, 1, 849.98), (3, 2, 69.98), (4, 3, 6.98);

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 799.99),
(1, 3, 2, 19.99),
(2, 4, 1, 49.99),
(2, 6, 2, 2.99),
(3, 5, 1, 3.99);