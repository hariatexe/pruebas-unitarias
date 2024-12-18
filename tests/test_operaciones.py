import allure; 
from src.operaciones import sumar,restar,multiplicar; 

@allure.epic("Test de operaciones")
@allure.feature("Operaciones de sumar, restar y multiplicar22")
@allure.description("Se realizaron operaciones basicas de 2 + 2, 2 - 2 y 10*10")

def test_sumar(): 
    resultado = sumar(2,2)
    assert resultado == 4


@allure.epic("Test de operaciones")
@allure.feature("Operacion de restar")
@allure.description("Se realizaron restas de 2 - 2")

def test_restar(): 
    resultado = restar(2,2)
    assert resultado == 0

@allure.epic("Test de operaciones")
@allure.feature("Operacion de multiplicar")
@allure.description("Multiplicacion de 10 * 10")

def test_multiplicar(): 
    resultado = multiplicar(10,10)
    assert resultado == 100

