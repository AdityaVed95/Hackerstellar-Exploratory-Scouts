import psycopg2

def get_count_customer_expense(customer_email):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pass",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        # Execute the query
        cursor.execute("SELECT COUNT(*) FROM (SELECT fk_customer_email FROM customer_expense WHERE fk_customer_email=%s) AS count_table;", (customer_email,))

        # Fetch result
        count = cursor.fetchone()[0]

        return count

    except (Exception, psycopg2.Error) as error:
        print("Error in fetching count", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# Example usage
count = get_count_customer_expense('e1@gmail.com')
print(count)
