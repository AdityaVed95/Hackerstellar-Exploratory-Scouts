# this fxn is useful when a new student creates their accoutn
# which is to added to the database 

import psycopg2

# this fxn returns 1,"1" tuple if the insertion was successful and 
#  0, error if it was not successful


def insert_investor_into_db(investorName,investorEmail,investorPassword,investorBudget,investorMobileNo,investorAddress,investorAge,investmentObjectiveId):
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
        
        insert into investor 
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s)

        """

        record_to_insert = (investorName, investorEmail,int(investorBudget),0,investorMobileNo,investorAddress,investorPassword,int(investorAge),investmentObjectiveId)

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
        
        

