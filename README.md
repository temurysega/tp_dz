# tp_dz

домашнее задание по технологиям программирования. задача следующая: разработать систему, которая управляет рецептамит. Позволяет создавать блюда, добавлять их в рецепты, масштабировать порции и генерировать список покупок 


# клонирование репо  
git clone https://github.com/temurysega/tp_dz.git 

cd tp_dz 


# установка зависимостей 
pip install -r requirements.txt 


# проверка тестов
pytest 

# также все классы рабочие можно импортировать в код 
from ingredient import Ingredient 

from recipe import Recipe 

from dietary_recipe import DietaryRecipe 

from shopping_list import ShoppingList

# Автор: Хурматуллин Тимур, группа: ББИ2508
