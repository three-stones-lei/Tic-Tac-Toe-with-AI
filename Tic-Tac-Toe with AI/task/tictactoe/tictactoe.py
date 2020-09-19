# write your code here
import random
class TicTacToe:
    coordinates = [[[1, 3], [2, 3], [3, 3]],
                   [[1, 2], [2, 2], [3, 2]],
                   [[1, 1], [2, 1], [3, 1]]]
    SIGN_X = 'X'
    SIGN_O = 'O'
    SIGN__ = '_'

    def __init__(self):
        self.field = TicTacToe.dispose_cells(9 * TicTacToe.SIGN__)
        self.first_move_X = None
        self.second_move_O = None

    def __str__(self):
        print('---------')
        for row in self.field:
            print(f'| {row[0]} {row[1]} {row[2]} |')
        print('---------')

    def dispose_cells(field_string):
        field_list = [' ' if element == '_' else element for element in list(field_string)]
        field = [[field_list[0], field_list[1], field_list[2]],
                 [field_list[3], field_list[4], field_list[5]],
                 [field_list[6], field_list[7], field_list[8]]]
        return field

    def judge_input_command(self):
        while True:
            command_list = input('Input command: ').split()
            if command_list[0] == 'exit':
                exit()
            if len(command_list) != 3:
                print('Bad parameters!')
                continue
            else:
                move_objects = ('easy', 'user', 'medium', 'hard')
                if any([command_list[0] != 'start', command_list[1] not in move_objects, command_list[2] not in move_objects]):
                    print('Bad parameters!')
                    continue
                else:
                    break
        self.first_move_X = command_list[1]
        self.second_move_O = command_list[2]
        self.__str__()

    def first_move_result(self, sign):
        if self.first_move_X == 'user':
            return self.user_move_result(sign)
        elif self.first_move_X == 'easy':
            return self.computer_move_result(sign, 'easy')
        elif self.first_move_X == 'medium':
            return self.computer_move_result(sign, 'medium')
        elif self.first_move_X == 'hard':
            return self.computer_move_result(sign, 'hard')

    def second_move_result(self, sign):
        if self.second_move_O == 'user':
            return self.user_move_result(sign)
        elif self.second_move_O == 'easy':
            return self.computer_move_result(sign, 'easy')
        elif self.second_move_O == 'medium':
            return self.computer_move_result(sign, 'medium')
        elif self.second_move_O == 'hard':
            return self.computer_move_result(sign, 'hard')

    def process_of_game(self):

        while True:
            first_result = self.first_move_result('X')
            if first_result == 'not finish':
                second_result = self.second_move_result('O')
                if second_result == 'not finish':
                    continue
                else:
                    print(second_result)
                    break
            else:
                print(first_result)
                break


    def user_move_result(self, sign):
        while True:
            insert_coordinate = input('Enter the coordinates:').split(' ')
            for element in insert_coordinate:
                if element.isdigit() == False:
                    print('You should enter numbers!')
                    break
            else:
                insert_coordinate = [int(element) for element in insert_coordinate]
                is_has_coordinate = False
                for i in range(len(TicTacToe.coordinates)):
                    for j in range(len(TicTacToe.coordinates[i])):
                        if TicTacToe.coordinates[i][j] == insert_coordinate:
                            if self.field[i][j] != ' ':
                                print('This cell is occupied! Choose another one!')
                                is_has_coordinate = True
                                break
                            else:
                                self.field[i][j] = sign
                                self.__str__()
                                return self.getResult(sign)
                    if is_has_coordinate == True:
                        break
                else:
                    print('Coordinates should be from 1 to 3!')

    def computer_move_result(self, sign, level):
        print(f'Making move level "{level}"')
        if level == 'easy':
            return self.computer_easy_move_result(sign)
        elif level == 'medium':
            return self.computer_medium_move_result(sign)
        elif level == 'hard':
            if self.first_move_X == 'hard':
                huPlayer = 'O'
                aiPlayer = 'X'
            elif self.second_move_O == 'hard':
                huPlayer = 'X'
                aiPlayer = 'O'
            return self.computer_hard_move_result(sign, huPlayer, aiPlayer)

    def computer_easy_move_result(self, sign):
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if self.field[i][j] == ' ':
                break
        self.field[i][j] = sign
        self.__str__()
        return self.getResult(sign)

    def computer_medium_move_result(self, sign):
        row_list = self.field
        column_list = [[self.field[i][j] for i in range(3)] for j in range(3)]
        incline_list = [[self.field[i][i] for i in range(3)], [self.field[i][3-1-i] for i in range(3)]]
        three_type = [row_list, column_list, incline_list]
        # move_strategy 1
        for type_list in three_type:
                for list in type_list:
                    if list.count(sign) == 2:
                        for element in list:
                            if element == ' ':
                                index = list.index(element)
                                index_list = type_list.index(list)
                                index_type = three_type.index(type_list)
                                if index_type == 0:
                                    i = index_list
                                    j = index
                                elif index_type == 1:
                                    j = index_list
                                    i = index
                                elif index_type == 2:
                                    if index_list == 0:
                                        i = index
                                        j = index
                                    elif index_list == 1:
                                        i = index
                                        j = 3 - 1 - i
                                self.field[i][j] = sign
                                self.__str__()
                                return self.getResult(sign)
        else:
            # move_strategy 2
            for type_list in three_type:
                for list in type_list:
                    if sign == 'X':
                        oppo_sign = 'O'
                    elif sign == 'O':
                        oppo_sign = 'X'
                    if list.count(oppo_sign) == 2:
                        for element in list:
                            if element == ' ':
                                index = list.index(element)
                                index_list = type_list.index(list)
                                index_type = three_type.index(type_list)
                                if index_type == 0:
                                    i = index_list
                                    j = index
                                elif index_type == 1:
                                    j = index_list
                                    i = index
                                elif index_type == 2:
                                    if index_list == 0:
                                        i = index
                                        j = index
                                    elif index_list == 1:
                                        i = index
                                        j = 3 - 1 - i
                                self.field[i][j] = sign
                                self.__str__()
                                return self.getResult(sign)
            else:
                # move_strategy 3
                return self.computer_easy_move_result(sign)

    def computer_hard_move_result(self, sign, huPlayer, aiPlayer):
        move = TicTacToe.minimax(self.field, sign, huPlayer, aiPlayer)
        i = move['index'][0]
        j = move['index'][1]
        self.field[i][j] = sign
        self.__str__()
        return self.getResult(sign)


    @staticmethod
    def winning(field, player):
        row_list = field
        column_list = [[field[i][j] for i in range(3)] for j in range(3)]
        incline_list = [[field[i][i] for i in range(3)], [field[i][3-1-i] for i in range(3)]]
        three_type = [row_list, column_list, incline_list]
        for type_list in three_type:
            for list in type_list:
                if list.count(player) == 3:
                    return True
        else:
            return False

    @staticmethod
    def minimax(field, player, huPlayer, aiPlayer):
        avail_spots = [element for row in field for element in row if element == ' ']
        if TicTacToe.winning(field, huPlayer):
            return {'score': -10}
        elif TicTacToe.winning(field, aiPlayer):
            return {'score': 10}
        elif len(avail_spots) == 0:
            return {'score': 0}
        moves = []
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == ' ':
                    move = {}
                    move['index'] = [i, j]
                    field[i][j] = player
                    if player == aiPlayer:
                        result = TicTacToe.minimax(field, huPlayer, huPlayer, aiPlayer)
                        move['score'] = result['score']
                    else:
                        result = TicTacToe.minimax(field, aiPlayer, huPlayer, aiPlayer)
                        move['score'] = result['score']
                    field[i][j] = ' '
                    moves.append(move)

        best_move = None
        if player == aiPlayer:
            best_score = -10000
            for i in range(len(moves)):
                if moves[i]['score'] > best_score:
                    best_score = moves[i]['score']
                    best_move = i
        elif player == huPlayer:
            best_score = 10000
            for i in range(len(moves)):
                if moves[i]['score'] < best_score:
                    best_score = moves[i]['score']
                    best_move = i
        return moves[best_move]


    def getResult(self, insert):
        row_list = self.field
        column_list = [[self.field[i][j] for i in range(3)] for j in range(3)]
        incline_list = [[self.field[i][i] for i in range(3)], [self.field[i][3-1-i] for i in range(3)]]
        three_type = [row_list, column_list, incline_list]
        is_have_empty = False
        for type_list in three_type:
            for list in type_list:
                if list.count(insert) == 3:
                    return f'{insert} wins'
                elif list.count(' ') != 0:
                    is_have_empty = True
        else:
            if is_have_empty == True:
                return 'not finish'
            else:
                return 'Draw'


while True:
    game = TicTacToe()
    game.judge_input_command()
    game.process_of_game()








