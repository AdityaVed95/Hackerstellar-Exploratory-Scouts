import psycopg2


def get_investment_options_details():
    connection = 0
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="navyanavya",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres",
                                      options="-c search_path=sy_mp,public")

        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from investment_option"
        
        cursor.execute(postgreSQL_select_Query)
        return cursor.fetchall()


    except (Exception, psycopg2.Error) as error:
        return "Error while fetching data from PostgreSQL " + str(error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
