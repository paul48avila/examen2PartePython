import psycopg2
#se conecta a la base de datos
try:

    conexion = psycopg2.connect(

        host = 'localhost',

        user = 'postgres',

        password = '123456',

        database = 'tienda'

    )

    print('Conexion exitosa')

    cursor=conexion.cursor()

    cursor.execute("SELECT version()")

    row=cursor.fetchone()

    print(row)

    cursor.execute("SELECT * FROM venta")


    rows=cursor.fetchmany()

    for row in rows:

        print(row)

except Exception as e:

    print('Error de conexion')

    print(e)

finally:

    conexion.close()

    print("Conexion finalizada")


#coneta a la base de datos con efectividad





#pasar un string a int
def string_to_int(string):
    try:
        return int(string)
    except ValueError:
        return None

#como sumar le valor strings ya que las devoluciones son en string y no en int

a= "2"
b= "3"

c= string_to_int(a) + string_to_int(b)
print(c)