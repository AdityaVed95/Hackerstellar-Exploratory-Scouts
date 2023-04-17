# # this fxn is useful when a user wishes to see the their personal
# # details on their profile page
#
# # this fxn returns 1 and the student details for the correct input and returns
# # 0 and the error in case of failed retreival of data
#
# import psycopg2
#
#
# def get_customer_details(customerEmail):
#     connection = 0
#     try:
#         connection = psycopg2.connect(user="postgres",
#                                       password="pass",
#                                       host="127.0.0.1",
#                                       port="5432",
#                                       database="postgres",
#                                       options="-c search_path=sy_mp,public")
#
#         cursor = connection.cursor()
#
#         postgreSQL_select_Query = "select * from customer where customer_email ='" + customerEmail + "'"
#         # 'select * from sy_mp.student where student_id =id2'
#         cursor.execute(postgreSQL_select_Query)
#         student_details = cursor.fetchall()
#         return student_details
#
#
#     except (Exception, psycopg2.Error) as error:
#         return "Error while fetching data from PostgreSQL " + str(error)
#
#     finally:
#         # closing database connection.
#         if connection:
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")

import psycopg2

def get_total_expense_cost(customerEmail):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        # Execute the query
        cursor.execute("SELECT SUM(expense_cost) FROM customer_expense WHERE fk_customer_email=%s;", (customerEmail,))

        # Fetch result
        total_cost = cursor.fetchone()[0]

        print(total_cost)

        return total_cost

    except (Exception, psycopg2.Error) as error:
        print("Error in fetching total cost", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Example usage
# total_cost = get_total_expense_cost('e1@gmail.com')
# print(total_cost)

if __name__ =="__main__":
    get_total_expense_cost('e1@gmail.com')

