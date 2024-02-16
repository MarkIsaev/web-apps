import subprocess
import pytest

# Указываем интерпретатор Python, который будет использоваться для запуска скриптов
INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    # Запуск скрипта filename с переданными данными input_data
    proc = subprocess.run(
        [INTERPRETER, filename], # Запускаем скрипт с указанным интерпретатором
        input='\n'.join(input_data if input_data else []), # Подаем ввод скрипту
        capture_output=True, # Захватываем вывод
        text=True, # Работаем с текстовым выводом
        check=False # Не проверяем код завершения процесса на ошибки
    )
    return proc.stdout.strip() # Возвращаем стандартный вывод скрипта без лишних пробелов

# Набор тестовых данных для каждого скрипта
test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird'),
    ],

    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ],


    'division': [
        (['1', '0'], ["Ошибка: деление на ноль"]),
        (['5',  '2'],[f"{5} // {2} = {5 // 2};"f"{5} / {2} = {5 / 2}"]),
        (['17',  '11'],[f"{17} // {11} = {17 // 11};"f"{17} / {11} = {17 / 11}"])
    ],
    'loops': [
        (['3'],['0', '1','4']),
        (['9'],['0','1','4','9','16','25','36','49','64']),
        (['-2'],[''])
    ],
    'print_function': [
        (['5'],['12345']),
        (['-2'],['']),
        (['11'],['1234567891011']),
        (["7"],["1234567"])
    ],
    'second_score': [
        (['5','2 3 6 6 5'], ['5']),
        (['6','4 1 3 4 6 4'],['4']),
        (['4','3 3 3 2'],['2'])
    ],
    'nested_list': [
        (["5","Гарри","37.21","Берри","37.21","Тина","37.2","Акрити","41","Харш","39",],['Берри','Гарри']),
        (["4","Кирилл","36.2","Олег","35","Пётр","34", "Вася", "36.2"],["Олег"]),
        (["6",'Олег','5','Пётр','6','Сергей','5','Алексей','4','Максим','8','Ира','5'],['Ира','Олег','Сергей'])
    ],
    "lists": [
        (["4","append 1","append 2","insert 1 3","print"],["[1, 3, 2]"]),
        (["12","insert 0 5","insert 1 10","insert 0 6","print","remove 6","append 9","append 1","sort","print","pop","reverse","print"],["[6, 5, 10]","[1, 5, 9, 10]","[9, 5, 1]"])
    ],
    "swap_case": [
        (["Www.MosPolytech.ru"], ["wWW.mOSpOLYTECH.RU"]),
        (["Pythonist 2"],["pYTHONIST 2"]),
        (["HFE.few:"],["hfe.FEW:"]),
        (["...P"],["...p"])
    ],
    "split_and_join":[
        (["this is a string"],["this-is-a-string"]),
        (["qwe gs eqwf fwee"],["qwe-gs-eqwf-fwee"]),
        (["Jfrw fwj fwlejl fewlnfew"],["Jfrw-fwj-fwlejl-fewlnfew"]),
        (["HE W:JC EJKED KDNWJ"],["HE-W:JC-EJKED-KDNWJ"]),
        ],
    "max_word":[
        ([],["сосредоточенности"])
        ],
    "price_sum":[
        ([],["6842.84 5891.06 6810.90"])
        ],
    "anagram":[
        (["hello", "le"],["YES"]),
        (["qwerty","yrn"],["NO"]),
        (["rf", "ewfrf"],["YES"]),
        (["rfk", "fewrerf"],["NO"])
        ],
    "metro":[
    (["5","2 10","4 19","3 7","13 70","1 50", "5"], ["4"]),
    (["4","5 7","1 4","12 167","32 67","4"],["1"]),
    (["7","4 1","6 7","12 54","32 54","4 6","3 6","34 64","7"],["1"])
    ],
    "minion_game":[
        (["BANANA"],["Стюарт 12"]),
        (["HDWLJCVEA"],["Стюарт 42"]),
        (["AEA"],["Кевин 6"])
    ],
    "is_leap":[
        (["1800"],["False"]),
        (["400"],["True"]),
        (["500"],["False"]),
        (["2004"],["True"]),
        (["2000"],["True"]),
        (["73"],["False"])
    ],
    "happiness":[
        (["3 2", "1 5 3", "3 1", "5 7"],["1"]),
        (["5 2","6 4 22","5 7","2 5"],["0"]),
        (["4 8", "4 43 1", "4 3", "2 6"],["1"])
    ],
    "pirate_ship":[
        (["4 5","яйцо 1 1", "огурец 1 1", "йогурт 1 1", "ожерелье 1 2", "клад 2 2"],["ожерелье 1.00 2.00", "клад 2.00 2.00", "йогурт 1.00 1.00"]),
        (["3 4","яйцо 5 5","огурец 6 7","йогург 5 2","клад 100 100","огурец 3.00 3.50"],["огурец 3.00 3.50"])
    ],
    "matrix_mult":[
        (["3","3 1 4","4 5 6","4 1 4","4 1 4","6 7 3","3 2 5"],["30 18 35", "64 51 61", "34 19 39"]),
        (["2", "4 5","7 3", "4 1", "7 4"],["51 24","49 19"]),
        (["4", "2 5 7 3","1 4 5 8", "4 1 9 0", "-4 1 4 6", "5 1 7 0", "4 5 1 5", "7 8 3 2", "3 6 8 2"],["88 101 64 45","80 109 90 46", "87 81 56 23", "30 69 33 25"]),      
    ]
}
# Каждый тест проверяет выполнение определенного скрипта с определенным входным данными и ожидаемым результато

# Пример теста для скрипта hello_world.py
def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

# Пример теста для скрипта python_if_else.py
def test_hello_world():
    assert run_script('hello.py') == 'Hello, world!'

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['max_word'])
def test_max_word(input_data, expected):
    assert run_script('max_word.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['price_sum'])
def test_price_sum(input_data, expected):
    assert run_script('price_sum.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

# Пример теста для скрипта
@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected
