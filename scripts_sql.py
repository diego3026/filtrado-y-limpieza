import filtrado
import conexion_db

conexion = conexion_db


class Insercion:

    def __init__(self):
        self.conexion = conexion_db.Conexion()
        self.conexion.conect()

    def insercion_inmueble(self, inmueble):
        self.conexion.execute('''INSERT INTO inmuebles(nombre,descripcion,estrato,cantidaddehabitaciones,
                              cantidaddeparqueaderos,piso,antiguedad,estado,areaprivada,areaconstruida,
                              precioadministracion,precio,idsector,iddireccion,idciudad,idtipoinmueble) 
                              VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', ())

    def insercion_usuario(self, usuario):
        self.conexion.execute('''INSERT INTO usuarios(nombre, apellido, edad, correo, contraseña,
                              codigodepaistelefonico, numerodetelefono) 
                              VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', ())
        
    def insercion_sectores(self, sector):
        self.conexion.execute("INSERT INTO sectores(nombre) VALUES (%s)", ())
        
    def insercion_inmueble_por_usuario(self, inmuebleporusuario):
        self.conexion.execute("INSERT INTO inmueblesporusuario(idusuario, idinmueble) VALUES (%s,%s)", ())
    
    def insercion_tipo_de_inmuebles(self, tipo_de_inmuebles):
        self.conexion.execute("INSERT INTO inmueblesporusuario(idusuario, idinmueble) VALUES (%s,%s)", ())
       
    def insercion_inmueble_por_usuario(self, inmueble):
        self.conexion.execute("INSERT INTO inmueblesporusuario(idusuario, idinmueble) VALUES (%s,%s)", ())
       
    def insercion_inmueble_por_usuario(self, inmueble):
        self.conexion.execute("INSERT INTO inmueblesporusuario(idusuario, idinmueble) VALUES (%s,%s)", ())
        
    def insercion_inmueble_por_usuario(self, inmueble):
        self.conexion.execute("INSERT INTO inmueblesporusuario(idusuario, idinmueble) VALUES (%s,%s)", ())
        
    def insercion_caracteristicas(self,caracteristicas):
        self.conexion.execute("INSERT INTO caracteristicas(nombre, ) VALUES (%s,%s)", ())
        
       