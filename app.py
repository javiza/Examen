from flask import Flask, render_template, request, session


app = Flask(__name__)

# configuracion de clave secreta
app.config['SECRET_KEY'] = '1234'

# Activa el modo depuracion
app.debug = True


# ruta para el home
@app.route('/')
def home():
    session['nombre'] = 'juan'
    return render_template('home.html')


# ruta para el ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # tomando los datos desde el formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        totalValor = 9000 * tarros
        # proceso de los datos
        if edad >= 18 and edad <= 30:

            totalDescuento = (totalValor * 15) / 100
            total = totalValor - totalDescuento
            nombre = f'Nombre del cliente: {nombre}'
            totalSinDescuento = f'Total sin descuento: ${totalValor}'
            descuento = f'El descuento es: ${totalDescuento}'
            totalPagar = f'El total a pagar es de: ${total}'
            return render_template('ejercicio1.html', nombre=nombre, totalSinDescuento=totalSinDescuento,
                                   descuento=descuento, totalPagar=totalPagar)
        elif edad > 30:
            totalDescuento = (totalValor * 25) / 100
            total = totalValor - totalDescuento
            nombre = f'Nombre del cliente: {nombre}'
            totalSinDescuento = f'Total sin descuento: ${totalValor}'
            descuento = f'El descuento es: ${totalDescuento}'
            totalPagar = f'El total a pagar es de: ${total}'
            return render_template('ejercicio1.html', nombre=nombre, totalSinDescuento=totalSinDescuento,
                                   descuento=descuento, totalPagar=totalPagar)
        else:
            totalDescuento = str("No aplica")
            nombre = f'Nombre del cliente: {nombre}'
            totalSinDescuento = f'Total sin descuento: ${totalValor}'
            descuento = f'El descuento es: {totalDescuento}'
            totalPagar = f'El total a pagar es de: ${totalValor}'
            return render_template('ejercicio1.html', nombre=nombre, totalSinDescuento=totalSinDescuento,
                                   descuento=descuento, totalPagar=totalPagar)
    return render_template('ejercicio1.html')


# ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # tomando los datos desde el formulario
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        # opcion administrador
        if nombre == 'juan' and contrasena == 'admin':
            session['nombre'] = nombre
            resultado = f'Bienvenido administrador {nombre}'
            return render_template('ejercicio2.html', resultado=resultado)
        # opcion usuario
        elif nombre == 'pepe' and contrasena == 'user':
            session['nombre'] = nombre
            resultado = f'Bienvenido usuario {nombre}'
            return render_template('ejercicio2.html', resultado=resultado)
        else:
            resultado = 'Nombre o contraseña equivocado'
            return render_template('ejercicio2.html', resultado=resultado)

    return render_template('ejercicio2.html')
# Ejecucion de la app
if __name__ == '__main__':
    app.run()
