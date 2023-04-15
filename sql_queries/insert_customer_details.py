# this fxn is useful when a new student creates their accoutn
# which is to added to the database 

import psycopg2

# this fxn returns 1,"1" tuple if the insertion was successful and 
#  0, error if it was not successful


def insert_customer_into_db(customerName, customerEmail, customerMobileNo, customerAddress, customerPassword, customerAge):
    connection = 0
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="navyanavya",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres",
                                    )

        cursor = connection.cursor()

        postgreSQL_insert_Query = """
        
        insert into customer 
        values(%s,%s,%s,%s,%s,%s)

        """

        record_to_insert = (customerName,customerEmail,customerMobileNo,customerAddress,customerPassword,int(customerAge))

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
        
        

