def test_function():
    def inner_function():
        print ('Я в области видимости функции test_function')
    inner_function()

#inner_function() - При вызове функции inner_function вне функции, будет ошибка,
#                   т.к. функция определена локально внутри функции test_function

test_function()     # Выводит функцию inner_function, содержащуюся в функции test_function

#Павел Ившин