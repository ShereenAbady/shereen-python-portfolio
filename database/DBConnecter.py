
import pymysql
from flask import current_app as app
from app.helpers import ResponseHandler as Helper

class DBConnector:
    """
    Database Connector Class for handling database operations.
    """
    
    def get_connection(self):
        """
        Establish a database connection and return (connection, cursor).
        """
        try:
            hostname = app.config["DB_HOST"]
            username = app.config["DB_USERNAME"]
            password = app.config["DB_PASSWORD"]
            db_name = app.config["DB_NAME"]
            
            connection = pymysql.connect(
                host=hostname,
                user=username,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor,
            )
            cursor = connection.cursor()
            return connection, cursor
        
        except Exception as e:
            Helper.error(f"Database connection error: {e}")
            return None, None

    
    def db_query(self,query="", query_type="read", fetch="one"):
        """
        Execute SQL queries and return the results.
        
        :param query: SQL query string.
        :param query_type: "read" for SELECT, "write" for INSERT/UPDATE/DELETE.
        :param fetch: "one" to fetch one row or "all" to fetch all rows (for read queries).
        :return: Query result or affected row count.
        """
        connection, cursor = None, None
        try:
            db_connector = DBConnector()
            connection, cursor = db_connector.get_connection()
            if not connection or not cursor:
                raise Exception("Failed to establish a database connection.")
            
            print('ok1')
            
            cursor.execute(query)
            result = None
            if query_type == "read":
                if fetch == "one":
                    result = cursor.fetchone()
                elif fetch == "all":
                    result = cursor.fetchall()
            elif query_type == "write":
                print('here2')
                connection.commit()
                result = cursor.rowcount
            
            return result
            
        except Exception as e:
            # You might want to log the error here or raise it
            raise Exception(f"Query error: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()