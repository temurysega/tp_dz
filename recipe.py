from ingredient import Ingredient
class Recipe:
  def __init__(self,title,  ingredients=None):
    self.title = title
    if ingredients is None:
      self.ingredients = []
    else: 
      self.ingredients = ingredients

  def add_ingredient(self, ingredient: Ingredient): 
    for exs in self.ingredients:
      if exs ==ingredient:
        exs.quantity+=ingredient.quantity
        return
    self.ingredients.append(ingredient)


  @staticmethod 
  def is_valid_ratio(ratio):
    return isinstance(ratio, (int, float)) and ratio > 0

  def scale(self, ratio: float): 
    if not self.is_valid_ratio(ratio):
        raise ValueError("отрицательное")
    newr= Recipe(self.title)
    for i in self.ingredients:
      sc = Ingredient(i.name, i.quantity *ratio, i.unit)
      newr.add_ingredient(sc)
    return newr 

  def __len__(self): 
    return len(self.ingredients)
  
  def __str__(self): 
    return f"{self.title}: {self.ingredients}" 
