import mysql.connector

def create_database():
    # Initialize connection to None
    conn = None
    
    try:
        # Connect to MySQL server without specifying database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="W9!s6Ql+.7"  
        )
        
        # Create cursor
        cursor = conn.cursor()
        
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close cursor and connection if they exist
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()