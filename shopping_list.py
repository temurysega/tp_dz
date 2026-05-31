from ingredient import Ingredient
from recipe import Recipe
class ShoppingList:
    def __init__(self):
        self._items =[]
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        sc= recipe.scale(portions)
        for ingredient in sc.ingredients:
            self._items.append((ingredient, recipe.title))
    

    def remove_recipe(self, title: str):
      mas= []
      for ingredient, rt in self._items:
        if rt != title:
            mas.append((ingredient, rt))
      self._items=mas

    def get_list(self):


        ito = {}

        for ingredient, rt in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in ito:
                ito[key] +=ingredient.quantity
            else:
                ito[key] = ingredient.quantity
        mas = []
        for (name, unit), quantity in ito.items():
            mas.append(Ingredient(name, quantity, unit))
        return sorted(mas, key=lambda ingredient: ingredient.name)

    def __add__(self, other):
        result = ShoppingList()
        for ingredient,rr in self._items +other._items:
            newc= Ingredient(ingredient.name, ingredient.quantity,ingredient.unit)
            result._items.append((newc, rr))
        return result
