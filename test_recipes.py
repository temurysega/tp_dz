import pytest
from ingredient import Ingredient
from recipe import Recipe
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



def test_recinit():
    rec = Recipe("Блины")
    assert rec.title =="Блины"
    assert rec.ingredients == []
def test_recadd():
    rec = Recipe("Блины")
    ing = Ingredient("Мука",500, "г")
    rec.add_ingredient(ing)
    assert len(rec.ingredients) == 1
    assert rec.ingredients[0]== ing
    assert rec.ingredients[0].quantity == 500.0
def test_recsame():
    rec = Recipe("Блины")
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Мука", 200, "г")
    rec.add_ingredient(ing1)
    rec.add_ingredient(ing2)
    assert len(rec.ingredients) ==1
    assert rec.ingredients[0].quantity ==700.0
def test_recsca():
    rec = Recipe("Блины")
    rec.add_ingredient(Ingredient("Мука", 500, "г"))
    rec.add_ingredient(Ingredient("Молоко", 300, "мл"))
    new = rec.scale(2)
    assert isinstance(new, Recipe)
    assert new is not rec
    assert new.ingredients[0].quantity ==1000.0
    assert new.ingredients[1].quantity == 600.0
    assert rec.ingredients[0].quantity == 500.0
    assert rec.ingredients[1].quantity== 300.0
def test_recscaer():
    rec = Recipe("Блины")
    with pytest.raises(ValueError):
        rec.scale(0)
    with pytest.raises(ValueError):
        rec.scale(-1)
def test_reclen():
    rec = Recipe("Блины")
    rec.add_ingredient(Ingredient("Мука", 500, "г"))
    rec.add_ingredient(Ingredient("Мука", 200, "г"))
    rec.add_ingredient(Ingredient("Молоко", 300,"мл"))
    assert len(rec) ==2
