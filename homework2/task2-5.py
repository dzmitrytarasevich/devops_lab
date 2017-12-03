N = 0
E = 1
S = 2
W = 3

# This function returns true if the given path is circular,
# else false
def isCircular(path):
    # Initialize starting point for robot as (0, 0) and starting
    # direction as N North
    x = 0
    y = 0
    dir = N

    # Traverse the path given for robot
    for i in xrange(len(path)):

        # Find current move
        move = path[i]

        # If move is left or right, then change direction
        if move == 'R':
            dir = (dir + 1) % 4
        elif move == 'L':
            dir = (4 + dir - 1) % 4

        # If move is Go, then change x or y according to
        # current direction
        else:  # if move == 'G'
            if dir == N:
                y += 1
            elif dir == E:
                x += 1
            elif dir == S:
                y -= 1
            elif dir == W:
                x -= 1

    return (x == 0 and y == 0)


# Driver program
path = "WWGLGLGLG"
if isCircular(path):
    print "Moves are circle"
else:
    print "Moves aren't circle"