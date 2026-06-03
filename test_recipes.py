from ingredient import Ingredient
def test_ingrinit():
    ing =Ingredient("Мука", 500, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"


def test_ingrstr():
    ing = Ingredient("Мука", 500, "г")


    assert str(ing) == "Мука: 500.0 г"
def test_ingresame():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 1000, "г")
    assert ing1 == ing2
def test_ingrrazn():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Сахар", 500, "г")
    assert ing1 != ing2


def test_ingrediffuni():
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 500, "кг")
    assert ing1 != ing2
