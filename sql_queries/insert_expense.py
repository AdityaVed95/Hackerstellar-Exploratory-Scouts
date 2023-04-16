import psycopg2

def insert_customer_expense(customer_email, expense_name, expense_type, expense_cost):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        # Execute the query with parameters
        cursor.execute("INSERT INTO customer_expense (fk_customer_email, expense_name, expense_type, expense_cost) VALUES (%s, %s, %s, %s);", (customer_email, expense_name, expense_type, expense_cost))

        # Commit the transaction
        connection.commit()

        print("Expense added successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error in inserting customer expense", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
