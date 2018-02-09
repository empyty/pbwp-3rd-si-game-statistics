
# Report functions

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



def get_most_played(file_name):
    '''Search for the most played game, by number of copies sold.'''
    games_list = list_of_elements(file_name)
    game_number = 0
    iteration = 0
    copies_sold = 0
    for i in range(len(games_list)):
        if games_list[i][1] > copies_sold:
            game_number = iteration
            copies_sold = games_list[i][1]
            iteration += 1
        else:
            iteration += 1
    return games_list[game_number][0]



def sum_sold(file_name):
    '''Returns summary of all the games in the file.'''
    games_list = list_of_elements(file_name)
    copies_sold = 0
    for i in range(len(games_list)):
        copies_sold += games_list[i][1]
    return copies_sold



def get_selling_avg(file_name):
    '''Return average sales of games in the file.'''
    games_list = list_of_elements(file_name)
    copies_sold = 0
    for i in range(len(games_list)):
        copies_sold += games_list[i][1]
    return copies_sold / len(games_list)



def count_longest_title(file_name):
    '''
    Search for the game, with the longest title.
    Return just it's length
    '''
    games_list = list_of_elements(file_name)
    game_number = 0
    iteration = 0
    game_name_length = 0
    for i in range(len(games_list)):
        if len(games_list[i][0]) > game_name_length:
            game_number = iteration
            game_name_length = len(games_list[i][0])
            iteration += 1
        else:
            iteration += 1
    return len(games_list[game_number][0])



def get_date_avg(file_name):
    '''Return average release date of games in the file, rounded up.'''
    games_list = list_of_elements(file_name)
    summary_release_dates = 0
    for i in range(len(games_list)):
        summary_release_dates += games_list[i][2]
    return round(summary_release_dates / len(games_list))



def get_game(file_name, title):
    '''Search for game data by title.'''
    games_list = list_of_elements(file_name)
    game_number = 0
    is_found = 0
    iteration = 0
    for i in range(len(games_list)):
        if title == games_list[i][0]:
            game_number = iteration
            is_found = 1
            return games_list[game_number]
        else:
            iteration += 1
    if is_found == 0:
        return 'Game not found'



def count_grouped_by_genre(file_name):
    '''Count genres and return a dictionary, with genre names and how many game of genre are there.'''
    games_list = list_of_elements(file_name)
    genre_list = {}
    for i in range(len(games_list)):
        if games_list[i][3] in genre_list:
            genre_list[games_list[i][3]] += 1
        else:
            genre_list[games_list[i][3]] = 1
    return genre_list



def get_date_ordered(file_name):
    games_list = list_of_elements(file_name)
    return games_list.sort(key=lambda x: x[2])
