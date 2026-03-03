-- PostgreSQL initialization script for Carmula

-- Create a new table for users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a new table for products
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a new table for orders
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount NUMERIC(10, 2) NOT NULL
);

-- Insert initial data into users table
INSERT INTO users (username, email, password_hash) VALUES
('admin', 'admin@carmula.com', 'hashed_password_here') ON CONFLICT (username) DO NOTHING;

-- Insert initial data into products table
INSERT INTO products (name, description, price) VALUES
('Example Product', 'This is an example product.', 19.99) ON CONFLICT (name) DO NOTHING;