
# Report functions

def count_games(file_name):
    '''Check how many lines is in the file, indicating number of games.'''
    with open(file_name, 'r') as input_list:
        return len(input_list.readlines())



def decide(file_name, year):
    '''Check if there is a game from a specific year in the file.'''
    games_list = list_of_elements(file_name)
    is_found = 0
    for i in range(len(games_list)):
        if year == games_list[i][2]:
            is_found = 1
            return True
    if is_found == 0:
        return 'No title found'



def get_latest(file_name):
    '''Search for a latest game in the file, return the one found first.'''
    games_list = list_of_elements(file_name)
    game_number = 0
    iteration = 0
    top_year = 0
    for i in range(len(games_list)):
        if games_list[i][2] > top_year:
            game_number = iteration
            top_year = games_list[i][2]
            iteration += 1
        else:
            iteration += 1
    return games_list[game_number][0]



def count_by_genre(file_name, genre):
    '''Check how many games in given genre are in the file.'''
    games_list = list_of_elements(file_name)
    total_games_in_genre = 0
    for i in range(len(games_list)):
        if str(genre) == games_list[i][3]:    
            total_games_in_genre += 1
    if total_games_in_genre > 0:        
        return total_games_in_genre
    else:
        return '0'



def get_line_number_by_title(file_name, title):
    '''Search for a specific title in the file, and return it's line number.'''
    games_list = list_of_elements(file_name)
    line_number = 1
    is_found = 0
    try:
        for i in range(len(games_list)):
            if title == games_list[i][0]:
                is_found = 1
                return line_number
            else:
                line_number += 1
        if is_found == 0:
            raise ValueError
    except ValueError:
        return 'No title found'



def list_of_elements(file_name):
    '''Read data from a file, and save it as a list easily readible for functions.'''
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
        for i in range(len(final_list_of_games)):
            final_list_of_games[i][1] = float(final_list_of_games[i][1])
            final_list_of_games[i][2] = int(final_list_of_games[i][2])
        return final_list_of_games



def get_genres(file_name):
    '''Return list of all genres in the list, without duplicates.'''
    games_list = list_of_elements(file_name)
    genres_list = []
    for i in range(len(games_list)):
        if games_list[i][3] in genres_list:
            continue
        else:
            genres_list.append(games_list[i][3])
    return sorted(genres_list)

def when_was_top_sold_fps(file_name):
    '''Check what was the release year of the top sold "First-person shooter game".'''
    games_list = list_of_elements(file_name)
    year_top_sold = 0
    sales = 0
    for i in range(len(games_list)):
        if games_list[i][3] == 'First-person shooter':
            if games_list[i][1] > sales:
                sales = games_list[i][1]
                year_top_sold = games_list[i][2]
    return year_top_sold
