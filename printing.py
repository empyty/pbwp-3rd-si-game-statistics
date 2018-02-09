import reports as rep
'''Use defined functions to print data in user-friendly way'''



file_name = 'game_stat.txt'



# How many games are in the file?
print('\nFile contains data of {} games.\n'.format(rep.count_games(file_name)))



# Is there a game from a given year?
# User input is necessary
while True:
    try:
        year = int(input('What year would you like to check?:\n'))
        if year < 1910 or year > 2030:
            raise ValueError
    except ValueError:
        print('Wrong input, try again.\n')
        continue
    break

# Print answer in user-friendly way

print(
    'There is a game from year {} on a list.\n'.format(year)
    if rep.decide(file_name, year) != 'No title found'
    else 'There is no game from {}.\n'.format(year))



# Which was the latest game?
print('The latest game on the list is {}.\n'.format(rep.get_latest(file_name)))



# How many games do we have by genre?
# User input is necessary

genre = input('What genre would you like to count?:\n')

# Print answer in user-friendly way

print(
    'There is 1 game in genre {}.\n'.format(genre)
    if rep.count_by_genre(file_name, genre) == 1
    else 'There are {} games in genre {}.\n'.format(rep.count_by_genre(file_name, genre), genre)
)



# What is the line number of the given game?
# User input is necessary

title = input('What game are you after?:\n')

# Print answer in user-friendly way

print(
    'The game {} is in line {}.\n'.format(title, rep.get_line_number_by_title(file_name, title))
    if rep.get_line_number_by_title(file_name, title) != 'No title found'
    else 'There is no game {} on the list\n'.format(title)
)



# What are the genres?

print('The genres on the list are:\n{}\n'.format(rep.get_genres(file_name)))


# What is the release date of the top sold "First-person shooter" game?

print('The realease date of the top sold FPS game is {}.\n'.format(rep.when_was_top_sold_fps(file_name)))