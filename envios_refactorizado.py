#envios_refactorizado.py
from abc import ABC, abstractmethod

CONFIG = {
    "PMAX": 45, "L1": 3, "L2": 10,
    "TARIFA_T1": 6000, "TARIFA_T2": 9000, "EXCEDENTE_KG": 800,
    "DESC_FRECUENTE": 0.05, "DESC_VIP": 0.10, "DESC_CUPON": 0.10,
    "RECARGO_FINDE": 2000, "MINIMO": 5000
}

class EstrategiaZona(ABC):
    @abstractmethod
    def calcular_recargo(self, base: float) -> float:
        pass

class ZonaUrbana(EstrategiaZona):
    def calcular_recargo(self, base: float) -> float: return 0

class ZonaRural(EstrategiaZona):
    def calcular_recargo(self, base: float) -> float: return base * 0.15

class ZonaNacional(EstrategiaZona):
    def calcular_recargo(self, base: float) -> float: return base * 0.40

class ZonaInsular(EstrategiaZona): 
    def calcular_recargo(self, base: float) -> float: return base * 0.70

def obtener_estrategia_zona(zona_str: str) -> EstrategiaZona:
    estrategias = {"urbana": ZonaUrbana(), "rural": ZonaRural(), 
                   "nacional": ZonaNacional(), "insular": ZonaInsular()}
    if zona_str not in estrategias:
        raise ValueError("zona invalida")
    return estrategias[zona_str]

def calc(peso, zona, cliente, dia, cupon=None): 
    if peso <= 0 or peso > CONFIG["PMAX"]:
        raise ValueError("peso invalido")
    if dia < 1 or dia > 7:
        raise ValueError("dia invalido")
    
    if zona == "insular" and cupon is not None:
        raise ValueError("Los envíos insulares no aceptan cupón")
    
    if peso <= CONFIG["L1"]:
        costo = CONFIG["TARIFA_T1"]
    elif peso <= CONFIG["L2"]:
        costo = CONFIG["TARIFA_T2"]
    else:
        costo = CONFIG["TARIFA_T2"] + (peso - CONFIG["L2"]) * CONFIG["EXCEDENTE_KG"]
    
    estrategia = obtener_estrategia_zona(zona)
    costo += estrategia.calcular_recargo(costo)
    
    if cliente == "frecuente":
        costo -= costo * CONFIG["DESC_FRECUENTE"]
    elif cliente == "vip":
        costo -= costo * CONFIG["DESC_VIP"]
    
    if cupon is not None:
        if zona == "insular": 
            raise ValueError("Los envíos insulares no aceptan cupón")
        if cupon == "ENVIO10":
            costo -= costo * CONFIG["DESC_CUPON"]
        else:
            raise ValueError("cupon invalido") 
    
    if dia >= 6:
        costo += CONFIG["RECARGO_FINDE"]
    
    if costo < CONFIG["MINIMO"]:
        costo = CONFIG["MINIMO"]
        
    return int((costo + 50) // 100 * 100)