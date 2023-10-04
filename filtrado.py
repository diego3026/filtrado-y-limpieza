import csv
import corregir_caracteres
import re
import insercionJson
from src.feats import Feats

file = open("./assets/csv/hotels.csv", mode="r", encoding="utf-8")
corregir_caracteres.corregir('./assets/csv/hotels.csv')

json_complete = insercionJson.JSONComplet()

csv_reader = csv.reader(file, delimiter=",")
line_count = 0
json = []

def get_location(fila:str):
    location = fila.split('-')
    return location

def convert_money(fila):
    match = re.findall(r'\d+', fila)
    money = ''.join(match)
    return money

def tratamiento_direccion(dir:str):
    if (dir.lower() =="preguntar al anunciante"):
        return None
    else:
        return dir
    

def get_caracteristicas(fila:str):
    lineas = fila.strip().split('\n')
    caracteristicas = []
    exterior = []
    interior = []
    sector = []
    bandera = None
    
    for linea in lineas:
        if linea == "Características del exterior":
            bandera = 0
        elif linea == "Características del interior":
            bandera = 1
        elif linea == "Características del sector":
            bandera = 2
        else:
            if bandera == 0 and linea != "":
                exterior.append(linea)
            elif bandera == 1 and linea != "":
                interior.append(linea)
            elif bandera == 2 and linea != "":
                sector.append(linea)
       
    caracteristicas = {'exterior':exterior, 'interior':interior, 'sector':sector}
    
    return caracteristicas
       

for row in csv_reader:
    if line_count == 0:
        line_count += 1
    elif line_count == 5:
        break
    else:
        Feats.filter(row=row[7])
        locations = get_location(row[2])
        if(row[10]!=""):
            lista = get_caracteristicas(row[10])
            insercion_dato = insercionJson.InsercionJson(url=row[0], name=row[1], sector=locations[0], ciudad=locations[1], departamento=locations[2],
                                                    tipo=row[4], descripcion=row[5],precio=convert_money(row[6]),caracteristicas=Feats.get_dictionary(),
                                                    direccion=tratamiento_direccion(row[8]),caracteristicasDelExterior=lista["exterior"],caracteristicasDelInterior=lista["interior"],
                                                    caracteristicasDelSector=lista["sector"])
        else:
            insercion_dato = insercionJson.InsercionJson(url=row[0], name=row[1], sector=locations[0], ciudad=locations[1], departamento=locations[2],
                                                    tipo=row[4], descripcion=row[5],precio=convert_money(row[6]),caracteristicas=Feats.get_dictionary(),
                                                    direccion=tratamiento_direccion(row[8]),caracteristicasDelExterior=None,caracteristicasDelInterior=None,
                                                    caracteristicasDelSector=None)

        json_complete.add_lista(insercion_dato)

        line_count += 1

