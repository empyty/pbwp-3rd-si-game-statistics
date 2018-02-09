import reports as rep

file_name = 'game_stat.txt'

def export_answers_to_file(file_name):
    with open("Judy's answers.txt", 'w') as ans_file:
        ans_file.write(str(rep.count_games(file_name)) + '\n')
        while True:
            try:
                year = int(input('What year would you like to check?:\n'))
                if year < 1910 or year > 2030:
                    raise ValueError
            except ValueError:
                print('Wrong input, try again.\n')
                continue
            break
        ans_file.write(str(rep.decide(file_name, year)) + '\n')
        ans_file.write(str(rep.get_latest(file_name)) + '\n')
        genre = input('What genre would you like to count?:\n')
        ans_file.write(str(rep.count_by_genre(file_name, genre)) + '\n')
        title = input('What game are you after?:\n')
        ans_file.write(str(rep.get_line_number_by_title(file_name,title)) + '\n')
        ans_file.write(str(rep.get_genres(file_name)) + '\n')
        ans_file.write(str(rep.when_was_top_sold_fps(file_name)) + '\n')

export_answers_to_file(file_name)