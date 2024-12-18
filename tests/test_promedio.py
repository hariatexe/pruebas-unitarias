import allure; 
from src.promedio import calcpromedio; 

@allure.epic("Test de calcular promedio")
@allure.feature("Lista de numeros")
@allure.description("Se calculo el promedio de una serie de numeros")
def test_promedio(): 
    numeros = [1,2,3,4,5]
    resultado = calcpromedio(numeros)
    assert resultado == 3; 