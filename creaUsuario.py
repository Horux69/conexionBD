import hashlib
from flask import Flask, render_template, request, redirect, flash
from flaskext.mysql import MySQL

programa = Flask(__name__)
programa.secret_key = 'clave_secreta'
mysql = MySQL()
programa.config['MYSQL_DATABASE_HOST'] = 'localhost'
programa.config['MYSQL_DATABASE_PORT'] = 3306
programa.config['MYSQL_DATABASE_USER'] = 'root'
programa.config['MYSQL_DATABASE_PASSWORD'] = ''
programa.config['MYSQL_DATABASE_DB'] = 'consulta'
mysql.init_app(programa)

conexion = mysql.connect()
cursor = conexion.cursor()

@programa.route('/')
def index():
    return render_template("login.html")

@programa.route('/guardar', methods=['GET', 'POST'])
def guardar():
    if request.method == 'POST':
        campos = ['idusuario', 'nombre', 'contrasena', 'activo']

        valores = {}
        for campo in campos:
            if campo == 'activo':
                valores[campo] = 1
            else:
                valor = request.form.get(campo)
                valores[campo] = valor

        if all(valores.values()):  # Verificar si todos los valores están presentes
            contrasena = valores['contrasena']
            encriptada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
            valores['contrasena'] = encriptada
# Esto es un comentario
            consulta = f"INSERT INTO usuarios ({', '.join(campos)}) VALUES ({', '.join(['%s'] * len(campos))})"
            valoresOrdenados = [valores[campo] for campo in campos]
            cursor.execute(consulta, valoresOrdenados)

            conexion.commit()

            flash("Los datos se han insertado correctamente.", "success")  # Mensaje flash de éxito
        else:
            # Si algún campo está vacío, se muestra un mensaje de error
            flash("Por favor, complete todos los campos.", "error")

        return redirect('/')

    else:
        return render_template('formulario.html')

if __name__ == '__main__':
    programa.run(host='0.0.0.0', debug=True, port='8080')
########################################################################################
# import hashlib
# from flask import Flask, render_template, request, redirect, flash
# from flaskext.mysql import MySQL

# programa = Flask(__name__)
# programa.secret_key = 'clave_secreta' 
# mysql = MySQL()
# programa.config['MYSQL_DATABASE_HOST'] = 'localhost'
# programa.config['MYSQL_DATABASE_PORT'] = 3306
# programa.config['MYSQL_DATABASE_USER'] = 'root'
# programa.config['MYSQL_DATABASE_PASSWORD'] = ''
# programa.config['MYSQL_DATABASE_DB'] = 'consulta'
# mysql.init_app(programa)

# conexion = mysql.connect()
# cursor = conexion.cursor()

# @programa.route('/')
# def index():
#     return render_template("login.html")

# @programa.route('/guardar', methods=['GET', 'POST'])
# def guardar():
#     if request.method == 'POST':
#         campos = ['idusuario', 'nombre', 'contrasena', 'activo']

#         valores = {}
#         for campo in campos:
#             if campo == 'activo':
#                 valores[campo] = 1
#             else:
#                 valor = request.form.get(campo)
#                 valores[campo] = valor

#         if 'contrasena' in valores:
#             contrasena = valores['contrasena']
#             encriptada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
#             valores['contrasena'] = encriptada

#             consulta = f"INSERT INTO usuarios ({', '.join(campos)}) VALUES ({', '.join(['%s'] * len(campos))})"
#             valoresOrdenados = [valores[campo] for campo in campos]
#             cursor.execute(consulta, valoresOrdenados)

#             conexion.commit()

#             flash("Los datos se han insertado correctamente.", "success")  # Mensaje flash de éxito

#         return redirect('/')

#     else:
#         return render_template('formulario.html')

# if __name__ == '__main__':
#     programa.run(host='0.0.0.0', debug=True, port='8080')











# import hashlib
# from flask import Flask, render_template, request, redirect, flash
# from flaskext.mysql import MySQL

# programa = Flask(__name__)
# programa.secret_key = 'clave_secreta' 
# mysql = MySQL()
# programa.config['MYSQL_DATABASE_HOST'] = 'localhost'
# programa.config['MYSQL_DATABASE_PORT'] = 3306
# programa.config['MYSQL_DATABASE_USER'] = 'root'
# programa.config['MYSQL_DATABASE_PASSWORD'] = ''
# programa.config['MYSQL_DATABASE_DB'] = 'consulta'
# mysql.init_app(programa)

# conexion = mysql.connect()
# cursor = conexion.cursor()

# @programa.route('/')
# def index():
#     return render_template("login.html")

# @programa.route('/guardar', methods=['GET', 'POST'])
# def guardar():
#     if request.method == 'POST':
#         campos = ['idusuario', 'nombre', 'contrasena', 'activo']

#         valores = {}
#         for campo in campos:
#             if campo == 'activo':
#                 valores[campo] = 1
#             else:
#                 valor = request.form.get(campo)
#                 valores[campo] = valor

#         if 'contrasena' in valores:
#             contrasena = valores['contrasena']
#             encriptada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
#             valores['contrasena'] = encriptada

#             consulta = f"INSERT INTO usuarios ({', '.join(campos)}) VALUES ({', '.join(['%s'] * len(campos))})"
#             valoresOrdenados = [valores[campo] for campo in campos]
#             cursor.execute(consulta, valoresOrdenados)

#             conexion.commit()

#             flash("Los datos se han insertado correctamente.", "success")  # Mensaje flash de éxito

#         return redirect('/')

#     else:
#         return render_template('formulario.html')

# if __name__ == '__main__':
#     programa.run(host='0.0.0.0', debug=True, port='8080')


# idusuario = input("Digite id: ")
# nombre = input("Digite nombre: ")
# contrasena = input("Digite contraseña: ")
# cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()

# sql = f"INSERT INTO usuarios (idusuario,nombre,contrasena,activo) VALUES ('{idusuario}','{nombre}','{cifrada}',1)"
# con = mysql.connect()
# cur = con.cursor()
# cur.execute(sql)
# con.commit()