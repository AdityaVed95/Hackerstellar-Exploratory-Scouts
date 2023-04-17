import psycopg2

def get_customer_expenses(customerEmail):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        # Execute the query
        cursor.execute("SELECT expense_name, expense_type, expense_cost FROM customer_expense WHERE fk_customer_email=%s;", (customerEmail,))

        # Fetch all rows
        rows = cursor.fetchall()

        return rows

    except (Exception, psycopg2.Error) as error:
        print("Error in fetching customer expenses", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


