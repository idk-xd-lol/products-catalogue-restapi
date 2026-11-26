# Product Catalogue

A simple web-based product catalogue built with **FastAPI**, **PostgreSQL**, **SQLAlchemy** and **Jinja2**. The application displays products on a homepage and provides a dedicated page for each product.

## Features

- Displays all products stored in a PostgreSQL database.
- Shows the total number of products.
- Product cards with images, prices and ratings.
- Dedicated product pages with additional details.
- Server-side HTML rendering using Jinja2.
- PostgreSQL database connection using SQLAlchemy.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Jinja2
- HTML / CSS

## Project Structure

```text
project/
├── app
│    ├── main.py
│    └── data/
│        └── database.py
├── frontend/
│   ├── index.html
│   ├── product.html
│   └── style.css
└── requirements.txt
```

## Database Setup

The application expects a PostgreSQL database with a `products` table.

### 1. Create a database

Create a database named `product_catalogue`:

```sql
CREATE DATABASE product_catalogue;
```

Connect to the database and create the table:

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image_url TEXT,
    price VARCHAR(100),
    rating NUMERIC(3, 2),
    rating_count INTEGER DEFAULT 0
);
```

### 2. Insert example data

```sql
INSERT INTO products (name, image_url, price, rating, rating_count)
VALUES
(
    'Example Product 1',
    'https://placehold.co/600x400',
    '99.99 USD',
    4.5,
    120
),
(
    'Example Product 2',
    'https://placehold.co/600x400',
    '149.99 USD',
    4.2,
    85
),
(
    'Example Product 3',
    'https://placehold.co/600x400',
    '49.99 USD',
    NULL,
    0
);
```

The example images are placeholders. Replace them with actual product image URLs.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/idk-xd-lol/products-catalogue-restapi.git
cd products-catalogue-restapi
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn uv sqlalchemy psycopg jinja2
```

## Database Configuration

The application uses the `DATABASE_URL` environment variable to connect to PostgreSQL.

Example:

```bash
export DATABASE_URL="postgresql+psycopg://username:password@localhost:5432/product_catalogue"
```

Replace `username` and `password` with your PostgreSQL credentials.

The connection URL format:

```text
postgresql+psycopg://USER:PASSWORD@HOST:PORT/DATABASE
```

| Parameter  | Description                                  |
| ---------- | -------------------------------------------- |
| `USER`     | PostgreSQL username                          |
| `PASSWORD` | PostgreSQL password                          |
| `HOST`     | Database server address, usually `localhost` |
| `PORT`     | PostgreSQL port, usually `5432`              |
| `DATABASE` | Database name                                |

The application reads this variable in `data/database.py`:

```python
import os
from sqlalchemy import create_engine

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
```

## Running the Application

Start the development server:

```bash
uv run fastapi dev
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

## Application Pages

| Route                           | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| `/`                             | Displays the product catalogue and total product count |
| `/products/{name}_{product_id}` | Displays an individual product page                    |

## Notes

- PostgreSQL must be running before starting the application.
- The `products` table must exist and contain data.
- The `DATABASE_URL` environment variable must be set.
- Product images are loaded from external image URLs.


