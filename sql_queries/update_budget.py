import psycopg2

def update_budget_prg(customerEmail,newBudget):
    try:
        connection = psycopg2.connect(user="sysadmin",
                                      password="pynative@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        cursor = connection.cursor()

        # Update single record now
        sql_update_query = """Update customer_budget set customer_budget_cost = %s where fk_customer_email = %s"""
        cursor.execute(sql_update_query, (price, mobileId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (mobileId,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

id = 3
price = 970
updateTable(id, price)
