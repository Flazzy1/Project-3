import psycopg2

conn = psycopg2.connect(dbname="test",user="postgres", password="1234567", host="localhost", port="5432")

cur = conn.cursor()

# Create Table
cur.execute("""
            CREATE TABLE IF NOT EXISTS dalhaz_users_using(
                id serial primary key,
                email text,
                name text,
                phone text,
                postalcode text
            )
            """)


# Inserting Data From CSV to Table
csv_file_path = r"A:\Data Engineering\Project 3\source\users_w_postal_code.csv"

with open(csv_file_path,"r") as f:
    next(f)
    cur.copy_from(file=f, table="dalhaz_users_using",sep=",", columns=("email", "name", "phone", "postalcode"))


conn.commit()