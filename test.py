import unittest
from task1 import analyse #импорт функций из задания 1 и 2
from task2 import calculate


class Testing(unittest.TestCase):

    def test_analyse_right(self): #тестируем функцию из задания 1, передавая ожидаемо верные параметры
        self.assertEqual(analyse([('принять', 46),('выгрузить', 46),('принять', 21),('выгрузить', 21),]), 4)
        self.assertEqual(analyse([('принять', 1), ('принять', 2), ('выгрузить', 1), ('принять', 3), ('принять', 4), ('выгрузить', 3), ]), 6)

    def test_analyse_wrong(self): #тестируем функцию из задания 1, передавая ожидаемо неверные параметры
        self.assertEqual(analyse([('принять', 46), ('выгрузить', 1), ('принять', 21), ('выгрузить', 21), ]), None) #со склада выгружают ящик, который не был загружен
        self.assertEqual(analyse([('принять', 1), ('принять', 1), ('выгрузить', 1), ]), None) #на склад загружено 2 одинаковых ящика
        self.assertEqual(analyse('s'), None) #Передан некорректный тип данных

    def test_calculate_right(self): #тестируем функцию из задания 2, передавая ожидаемо верные параметры
        self.assertEqual(calculate(3,3, [6,2,3]), 12)
        self.assertEqual(calculate(3,3, [2,4,8]), 14)
        self.assertEqual(calculate(5,5, [8,6, 1,2,3]), 28)

    def test_calculate_wrong(self): #тестируем функцию из задания 2, передавая ожидаемо неверные параметры
        self.assertEqual(calculate(1, 5, [8, 6, 1, 2, 3]), None) #количество дней != количеству уровней
        self.assertEqual(calculate(5, 5, [1, 2, 3]), None) #длина списка бонусов != количеству уровней
        self.assertEqual(calculate(5, 5, ['8', 6, '1', 2, True]), None) #Передан некорректный тип данных

if __name__ == "__main__":
  unittest.main()


