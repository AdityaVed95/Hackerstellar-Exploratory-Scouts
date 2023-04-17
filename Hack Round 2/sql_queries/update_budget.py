import psycopg2

def update_budget_prg(customerEmail,newBudget):
    connection = None
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        # Update single record now
        sql_update_query = """Update customer_budget set customer_budget_cost = %s where fk_customer_email = %s"""
        cursor.execute(sql_update_query, (newBudget, customerEmail))

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


