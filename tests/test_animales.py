import allure
from src.animales import nombres_animales; 


#test donde se devuelve una lista de nombres de animal
@allure.epic("Listas de nombre")
@allure.feature("Animales")
@allure.description("Hola como estas esta es mi primera vez con allure")

def test_nombres(): 
    resultado = nombres_animales(); 
    assert isinstance(resultado,list)


@allure.epic("Listas de nombre")
@allure.feature("Animales")
@allure.description("Error a propósito")
def test_nombres2(): 
    resultado2 = nombres_animales(); 
    assert isinstance(resultado2,str)