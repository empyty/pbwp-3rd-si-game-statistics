import reports as rep
'''Use defined functions to print data in user-friendly way'''



file_name = "game_stat.txt"



# What is the title of the most played game, based on sales

print('\nThe most played game based on sales is {}.\n'.format(rep.get_most_played(file_name)))



# How many games have been sold total

print('Games from the list have been sold in {} copies total.\n'.format(rep.sum_sold(file_name)))



# What is the average selling of games in the file

print('Games have been sold in average {}mln copies.\n'.format(rep.get_selling_avg(file_name)))



# How many characters long is the longest title

print('The longest title in the file is {} characters long.\n'.format(rep.count_longest_title(file_name)))



# What is the average of release dates

print('Games have been released in average in {}.\n'.format(rep.get_date_avg(file_name)))



# What properties has a game searched by title

title = input('What game are you after?:\n')

print(
    "The game you're after is {}\n".format(rep.get_game(file_name, title))
    if rep.get_game(file_name, title) != 'Game not found'
    else "That game isn't in the file.\n")



# How many games are there grouped by genre

print("Number of games in genres are as follows \n{}\n".format(rep.count_grouped_by_genre(file_name)))