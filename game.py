"""
Elijah Fabon
A01324170
"""


def game(): # called from main
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        # // Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice( )
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
            if character_has_leveled():
                execute_glow_up_protocol()
                achieved_goal = check_if_goal_attained(board, character)
        else:
            # // Tell the user they can’t go in that direction
            # // Print end of game stuff like congratulations or sorry you died