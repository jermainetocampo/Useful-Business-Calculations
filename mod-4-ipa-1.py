'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph:
        fromMemberfollower = social_graph[from_member]['following']
    else:
        fromMemberfollower = [ ]
        
    #to check the following of to_member
    if to_member in social_graph:
        toMemberfollower = social_graph[to_member]['following']
    else:
        toMemberfollower = [ ]
        

    if  (from_member in toMemberfollower) and (to_member in fromMemberfollower):
        status = "friends"
    
    elif to_member in fromMemberfollower:
        status = "follower"
        
    elif from_member in toMemberfollower:
        status = "followed by"
    
    else:
        status = "no relationship"
        
    return status
    


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    horizontal_list = []
    vertical_list = []
    a = len(board)
    
    #to make the board for the vertical
    vertical_board = [x for x in zip(*board)]
    
    #to make into a set so that i can check later on if there is a win
    for x in range(0,a):
        horizontal = set(board[x])
        horizontal_list.append(horizontal)
    
    for x in range(0,a):
        vertical = set(vertical_board[x])
        vertical_list.append(vertical)
    
    diagonal_ud = set([board[i][i] for i,v in enumerate(board)])
    diagonal_du = set([board[a-1-i][i] for i,v in enumerate(board1)])
    
    #checking the set if there's a winner (we know there is a winner if in the list there is a set that has a length of 1)
    for y in range(0,len(horizontal_list)):
        len_h = len(horizontal_list[y]) 
    
        if len_h == 1:
            symbol = horizontal_list[y]
            winner = ', '.join(symbol)
            break
        else:
            for y in range(0,len(vertical_list)):
                len_v = len(vertical_list[y]) 
    
                if len_v == 1:
                    symbol = vertical_list[y]
                    winner = ', '.join(symbol)
                    break
                
                else:
                    if len(diagonal_ud) == 1:
                        symbol = diagonal_ud
                        winner = ', '.join(symbol)

                    elif len(diagonal_du) == 1:
                        symbol = diagonal_du
                        winner = ', '.join(symbol)

                    else:
                        winner = "NO WINNER"
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    
    if (first_stop,second_stop) in legs:
        time = legs[(first_stop,second_stop)]['travel_time_mins']
        travel_time = time

    else:
        x = legs.keys() 
        y = list(x)
        
        for i in range(0,len(legs)):
                if y[i][0] is first_stop:
                    time = legs[y[i]]['travel_time_mins']
                    travel_time += time
                    i+=1
                    if i >= len(legs):
                            i = 0
                    while y[i][1] is not second_stop:
                        time = legs[y[i]]['travel_time_mins']
                        travel_time += time
                        i+=1
                        if i >= len(legs):
                            i = 0
                elif y[i][1] is second_stop:
                    time = legs[y[i]]['travel_time_mins']
                    travel_time += time      
                
    return travel_time