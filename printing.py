import reports as rep

file_name = 'game_stat.txt'

print('File contains data of {} games.'.format(rep.count_games(file_name)))

year = 2013
print(
    'There is a game from year {} on a list.'.format(year)
    if rep.decide(file_name, year)
    else 'There is no game from {}.'.format(year))

print('The latest game on the list is {}.'.format(rep.get_latest(file_name)))

genre = 'First-person shooter'
print(
    'There is 1 game in genre {}.'.format(genre)
    if rep.count_by_genre(file_name, genre) == 1
    else 'There are {} games in genre {}.'.format(rep.count_by_genre(file_name, genre), genre)
)

title = "Counter-Strike"
print(
    'The game {} is in line {}.'.format(title, rep.get_line_number_by_title(file_name, title))
    if rep.get_line_number_by_title(file_name, title) > 0
    else 'There is no game {} on the list'.format(title)
)

print('The genres on the list are: {}'.format(rep.get_genres(file_name)))

print('The realease date of the top sold FPS game is {}.'.format(rep.when_was_top_sold_fps(file_name)))