import json
import re

class Feats:

    def valor_numerico(fila):
        match = re.findall(r'\d+', fila)
        valor = ''.join(match)
        return int(valor)
    
    def valor_antiguedad(antiguedad):
        match = re.findall(r'\d+', antiguedad)
        # valor = ''.join(match)
        if(len(match)==2):
            valor_promedio = (int(match[0]) + int(match[1]))/2
            return valor_promedio
        elif(len(match)==1):    
            valor = int(match[0])
            return valor
        
    def comprobar_error(validar):
        try:
            return validar
        except:
            return None
        
    @classmethod
    def filter(self,row:str):
        list_row = eval(row)
        try:
            self.habitaciones = int(list_row[1]['Habitaciones'])
            self.baños = int(list_row[2]['Baños'])
            self.parqueaderos = int(list_row[3]['Parqueaderos'])
            self.area_construida = self.valor_numerico(list_row[4]['Área construída'])
            self.area_privada = self.valor_numerico(list_row[5]['Área privada'])
            self.estrato = list_row[6]['Estrato']
            self.antiguedad = self.valor_antiguedad(list_row[7]['Antigüedad'])
            self.numero_piso = int(list_row[8]['Piso N°'])
            self.administracion = self.valor_numerico(list_row[9]['Administración'])
            self.precio_m2 = self.valor_numerico(list_row[10]['Precio m²'])            
        except:
            pass
        
    @classmethod
    def get_dictionary(self):
        dictionary = {
            'habitaciones': self.habitaciones,
            'baños': self.baños,
            'parqueaderos': self.parqueaderos,
            'area_construida': self.area_construida,
            'area_privada': self.area_privada,
            'estrato': self.estrato,
            'antiguedad': self.antiguedad,
            'numero_piso': self.numero_piso,
            'administracion': self.administracion,
            'precio_m2': self.precio_m2
        }
        return dictionary
