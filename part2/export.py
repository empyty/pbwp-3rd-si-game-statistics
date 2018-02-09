import reports as rep

file_name = 'game_stat.txt'

def export_answers_to_file(file_name):
    with open("Judy's answers.txt", "w") as ans_file:
        ans_file.write(str(rep.get_most_played(file_name)) + '\n')
        ans_file.write(str(rep.sum_sold(file_name)) + '\n')
        ans_file.write(str(rep.get_selling_avg(file_name)) + '\n')
        ans_file.write(str(rep.count_longest_title(file_name)) + '\n')
        ans_file.write(str(rep.get_date_avg(file_name)) + '\n')
        title = input('What game are you after?:\n')
        ans_file.write(str(rep.get_game(file_name, title)) + '\n')

export_answers_to_file(file_name)