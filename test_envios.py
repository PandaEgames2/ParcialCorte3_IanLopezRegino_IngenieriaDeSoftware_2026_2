"""
Suite de Pruebas 22 Casos - Parcial 3 Ingeniería de Software
Estudiante: Código 310059
Cubre: 100% ramas independientes, Reglas R1-R9, Paridad (D,E,B,F), Zona Insular
"""

import pytest
from envios_refactorizado import calc

casos_prueba = [
    # 1. PARTICIONES INVÁLIDAS Y LÍMITES
    (0, "urbana", "normal", 1, None, ValueError),           
    (45.1, "urbana", "normal", 1, None, ValueError),        
    (2, "lunar", "normal", 1, None, ValueError),            
    (2, "urbana", "normal", 8, None, ValueError),           
    (2, "urbana", "normal", 1, "FALSO", ValueError),        
    
    # 2. CÁLCULO BASE POR TRAMOS (L1=3, L2=10)
    (3, "urbana", "normal", 1, None, 6000),                 
    (3.1, "urbana", "normal", 1, None, 9000),               
    (10, "urbana", "normal", 1, None, 9000),                
    (11, "urbana", "normal", 1, None, 9800),                
    
    # 3. RECARGOS DE ZONA (RR=15%, RN=40%)
    (2, "rural", "normal", 1, None, 6900),                  
    (2, "nacional", "normal", 1, None, 8400),               
    
    # 4. DESCUENTOS Y FIN DE SEMANA (Reglas B y E)
    (2, "urbana", "frecuente", 1, None, 5700),              
    (2, "urbana", "vip", 1, None, 5400),                    
    (2, "urbana", "normal", 1, "ENVIO10", 5400),            
    (2, "urbana", "normal", 6, None, 8000),                 
    (10, "nacional", "vip", 6, "ENVIO10", 12200),           
    
    # 5. MÍNIMO GARANTIZADO Y REDONDEO BANCARIO (Regla R8)
    (1, "urbana", "vip", 1, "ENVIO10", 6000),               
    (10.1, "urbana", "normal", 1, None, 9100),              
    (5, "rural", "frecuente", 1, "ENVIO10", 8800),          
    (45, "urbana", "vip", 1, "ENVIO10", 29900),             
    
    # 6. EVOLUCIÓN: ZONA INSULAR (CAMBIO = 0)
    (2, "insular", "normal", 1, None, 10200),               
    (2, "insular", "normal", 1, "ENVIO10", ValueError),     
]

@pytest.mark.parametrize("p, z, c, d, cup, esperado", casos_prueba)
def test_calc(p, z, c, d, cup, esperado):
    if esperado == ValueError:
        with pytest.raises(ValueError):
            calc(p, z, c, d, cup)
    else:
        assert calc(p, z, c, d, cup) == esperado