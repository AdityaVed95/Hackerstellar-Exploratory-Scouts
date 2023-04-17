import psycopg2

def delete_expense_prg(fkCustomerEmail, expenseName):
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        # Create a cursor object
        cur = conn.cursor()

        # Define the delete query with placeholders for parameters
        delete_query = "DELETE FROM customer_expense WHERE fk_customer_email=%s AND expense_name=%s"

        # Execute the delete query with parameters
        cur.execute(delete_query, (fkCustomerEmail, expenseName))

        # Commit the transaction
        conn.commit()



    except (Exception, psycopg2.Error) as error:
        print("Error while deleting expense:", error)

    finally:
        # Close the database connection and cursor
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")
