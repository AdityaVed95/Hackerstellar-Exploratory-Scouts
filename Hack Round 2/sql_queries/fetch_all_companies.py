# this fxn is useful when a user wishes to see the their personal
# details on their profile page

# this fxn returns 1 and the student details for the correct input and returns
# 0 and the error in case of failed retreival of data

import psycopg2


def get_all_company_details():
    connection = 0
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres",
                                      options="-c search_path=sy_mp,public")

        cursor = connection.cursor()

        postgreSQL_select_Query = "select * from company"
        
        cursor.execute(postgreSQL_select_Query)
        company_names = cursor.fetchall()
        return company_names


    except (Exception, psycopg2.Error) as error:
        return "Error while fetching data from PostgreSQL " + str(error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
