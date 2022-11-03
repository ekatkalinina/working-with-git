def print_players_with_5_matches(file_name: str):
    """
    Выводит данные о футболистах, которые участвовали более чем в 5 играх
    :param file_name: название файла, содержащий сведения о футболистах
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
    football_players = data.split('\n')
    counter = 1
    for player in football_players:
        entry = player.split('\t')
        print(f'{counter}. ФИО: {entry[0]} {entry[1]} {entry[2]}. Дата рождения: {entry[4]}. Кол-во игр: {entry[3]}')
        counter += 1


def count_players_with_5_matches(file_name: str) -> int:
    """
    Находит количество футболистов, которые участвовали более чем в 5 играх
    :param file_name: название файла, содержащий сведения о футболистах
    :return: количество футболистов, которые участвовали более чем в 5 играх
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
    football_players = data.split('\n')
    counter = 0
    for player in football_players:
        entry = player.split('\t')
        if int(entry[3]) > 5:
            counter += 1
    return counter


if __name__ == '__main__':
    print_players_with_5_matches('file.txt')
    print(f"{count_players_with_5_matches('file.txt')} футболистов участвовали более чем в 5 играх.")
