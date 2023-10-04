class InsercionJson:
    def __init__(self, url=None, name=None, sector=None, ciudad=None, departamento=None,
                 pais="colombia", tipo=None, descripcion=None, precio=None, caracteristicas=None,
                 direccion=None, caracteristicasDelExterior=None, caracteristicasDelInterior=None, caracteristicasDelSector=None):
        self.url= url
        self.name= name
        self.sector= sector
        self.ciudad= ciudad
        self.departamento= departamento
        self.pais= pais
        self.tipo= tipo
        self.descripcion= descripcion
        self.precio= precio
        self.caracteristicas= caracteristicas
        self.direccion= direccion
        self.caracteristicasDelExterior= caracteristicasDelExterior
        self.caracteristicasDelInterior= caracteristicasDelInterior
        self.caracteristicasDelSector= caracteristicasDelSector


    def json_unico(self):
        jsonUnic = {
            'url': self.url,
            'name': self.name,
            'sector': self.sector,
            'ciudad': self.ciudad,
            'departamento': self.departamento,
            'pais': self.pais,
            'tipo': self.tipo,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'caracteristicas': self.caracteristicas,
            'direccion': self.direccion,
            'caracteristicasDelExterior': self.caracteristicasDelExterior,
            'caracteristicasDelInterior': self.caracteristicasDelInterior,
            'caracteristicasDelSector': self.caracteristicasDelSector,
        }
        return jsonUnic
    
        
class JSONComplet:
    
    def __init__(self):
        self.lista_dato = []
        
    def add_lista(self, dato):
        self.lista_dato.append(dato)
        
    def show_lista(self):
        return self.lista_dato