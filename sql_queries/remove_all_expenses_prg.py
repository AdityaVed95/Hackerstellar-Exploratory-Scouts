

import psycopg2



def remove_all_responses_from_db_for_given_customerEmail(customerEmail):
    connection = 0
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres",
                                      )

        cursor = connection.cursor()

        postgreSQL_delete_Query = "Delete from customer_expense where fk_customer_email ='"+ customerEmail +"'"

        cursor.execute(postgreSQL_delete_Query,)

        connection.commit()

        return 1,"1"

    except (Exception, psycopg2.Error) as error:
        return 0,"Error while inserting data into PostgreSQL : "+ str(error)


    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



