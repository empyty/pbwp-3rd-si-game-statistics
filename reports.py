
# Report functions

def count_games(file_name):
    with open(file_name, 'r') as input_list:
        return len(input_list.readlines())

def decide(file_name, year):
    with open(file_name, 'r') as input_list:
        for i in input_list:
            if str(year) in i:
                return True

def get_latest(file_name):
    listed_games = list_of_elements(file_name)
    game_number = 0
    iteration = 0
    top_year = 0
    for i in range(len(listed_games)):
        if int(listed_games[i][2]) > top_year:
            game_number = iteration
            top_year = int(listed_games[i][2])
            iteration += 1
        else:
            iteration += 1
    return listed_games[game_number][0]

def count_by_genre(file_name, genre):
    total_games_in_genre = 0
    with open(file_name, 'r') as input_list:
        for i in input_list:
            if genre in i:
                total_games_in_genre += 1
        return total_games_in_genre

def get_line_number_by_title(file_name, title):
    line_number = 1
    with open(file_name, 'r') as input_list:
        try:
            for i in input_list:
                if str(title) in i:
                    return line_number
                else:
                    line_number += 1
            if line_number == 1:
                raise ValueError
        except ValueError:
            return('No title found.')

def list_of_elements(file_name):
    with open(file_name, 'r') as file:
        how_long_is_list = len(file.readlines())
        file.seek(0)
        listed_file_items = [[file.readline()] for i in range(how_long_is_list)]
        separated_values_in_list = []
        clean_list_of_games = []
        final_list_of_games = []
        for i in listed_file_items:
            for j in i:
                separated_values_in_list.append([j.replace('\t', ', ')])
        for i in separated_values_in_list:
            for j in i:
                clean_list_of_games.append([j.replace('\n', '')])
        for i in clean_list_of_games:
            for j in i:
                final_list_of_games.append(j.split(', '))
        return final_list_of_games

def get_genres(file_name):
    games_list = list_of_elements(file_name)
    genres_list = []
    for i in range(len(games_list)):
        if games_list[i][3] in genres_list:
            continue
        else:
            genres_list.append(games_list[i][3])
    return sorted(genres_list)

def when_was_top_sold_fps(file_name):
    games_list = list_of_elements(file_name)
    year_top_sold = 0
    sales = 0
    for i in range(len(games_list)):
        if games_list[i][3] == 'First-person shooter':
            if float(games_list[i][1]) > sales:
                sales = float(games_list[i][1])
                year_top_sold = int(games_list[i][2])
    return year_top_sold
