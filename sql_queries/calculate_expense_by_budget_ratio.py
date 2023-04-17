import psycopg2


def get_budget_details(customerEmail):
    connection = 0
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres",
                                      options="-c search_path=sy_mp,public")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select customer_budget_cost from customer_budget where fk_customer_email ='" + customerEmail + "'"
        # 'select * from sy_mp.student where student_id =id2'
        cursor.execute(postgreSQL_select_Query)
        budget = cursor.fetchall()
        budget_num = budget[0][0]

        cursor = connection.cursor()
        cursor.execute("SELECT SUM(expense_cost) FROM customer_expense WHERE fk_customer_email=%s;", (customerEmail,))
        total_cost = cursor.fetchone()[0]

        ratio = total_cost/budget_num
        return ratio


    except (Exception, psycopg2.Error) as error:
        return "Error while fetching data from PostgreSQL " + str(error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
