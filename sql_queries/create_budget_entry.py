# insert into budget table
import psycopg2
def insert_customer_into_db(customerEmail):
    connection = 0
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres",
                                      )

        cursor = connection.cursor()

        postgreSQL_insert_Query = """
        
        insert into customer_budget 
        values(%s,%s)

        """

        record_to_insert = (customerEmail,0)

        cursor.execute(postgreSQL_insert_Query,record_to_insert)

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



