def isCircular(path):
    x = 0
    y = 0
    for i in xrange(len(path)):
        move = path[i]
        if move == 'U':
                y += 1
        elif move == 'D':
                y -= 1
        elif move == 'R':
                x += 1
        elif move == 'L':
                x -= 1
    return (x == 0 and y == 0)
path = "UURDDL"
if isCircular(path):
    print "true"
else:
print "false"
