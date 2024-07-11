from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2 import sql
import bcrypt

# Database connection parameters
db_params = {
    'user': 'postgres',
    'host': 'localhost',
    'database': 'dahwin',
    'password': '5779ra',
    'port': 5432,
}

app = FastAPI()

def connect_db():
    """Establish a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_user_table():
    """Create a table for storing user information."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                date_of_birth DATE,
                gender VARCHAR(10),
                country VARCHAR(50),
                email VARCHAR(100) UNIQUE,
                password VARCHAR(100)
            );
            '''
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            conn.close()
            print("User table created successfully.")
        except Exception as e:
            print(f"Error creating user table: {e}")

def hash_password(password):
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(hashed_password, user_password):
    """Check a hashed password."""
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

def signup_user(name, date_of_birth, gender, country, email, password):
    """Sign up a new user and store their information in the database."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            hashed_password = hash_password(password)
            insert_query = '''
            INSERT INTO users (name, date_of_birth, gender, country, email, password)
            VALUES (%s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(insert_query, (name, date_of_birth, gender, country, email, hashed_password))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error signing up user: {e}")
            return False

def login_user(email, password):
    """Login a user by verifying their credentials."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            select_query = '''
            SELECT password FROM users WHERE email = %s;
            '''
            cursor.execute(select_query, (email,))
            stored_password = cursor.fetchone()
            cursor.close()
            conn.close()
            if stored_password and check_password(stored_password[0], password):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error logging in user: {e}")
            return False

class UserSignup(BaseModel):
    name: str
    date_of_birth: str
    gender: str
    country: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@app.on_event("startup")
def on_startup():
    create_user_table()

@app.post("/signup")
def signup(user: UserSignup):
    if signup_user(user.name, user.date_of_birth, user.gender, user.country, user.email, user.password):
        return {"message": "User signed up successfully."}
    else:
        raise HTTPException(status_code=400, detail="Error signing up user.")

@app.post("/login")
def login(user: UserLogin):
    if login_user(user.email, user.password):
        return {"message": "Login successful."}
    else:
        raise HTTPException(status_code=400, detail="Login failed. Invalid email or password.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
