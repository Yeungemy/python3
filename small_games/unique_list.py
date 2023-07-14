def unique_list(my_list):
    # game_board = []
    # test = 0
    # for num in my_list:
    #     if test != num:
    #         test = num
    #         game_board.append(num)
    # return game_board
    
    return list(set(my_list))


print(unique_list([1, 1, 2,2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7]))
