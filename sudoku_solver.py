#an example for an unsolved board
board = [
    [9,0,0,0,0,0,0,6,0],
    [0,0,0,0,8,0,1,9,0],
    [0,0,7,0,1,0,0,0,0],
    [0,0,0,0,0,6,0,7,3],
    [0,0,0,3,0,9,0,0,0],
    [3,4,5,0,0,0,0,0,0],
    [4,0,0,0,0,2,6,8,0],
    [0,0,2,5,0,0,0,0,0],
    [0,3,0,7,0,0,0,0,0]
]

#print_board prints the 9*9 sudoko board in a visual way
def print_board(bo):
     
     for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        
        for j in range(len(bo[0])):

            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(bo[i][j])

            else:
                print((str(bo[i][j])) + " ", end="")

#solver solves the board essentially 
def solver(bo):

    look_up = find_empty(bo)

    if not look_up:
        return True
    else:
        (row , column) = look_up

    for i in range(1,10):
        if valid(bo, i, (row, column)):
            bo[row][column] = i 

            if solver(bo):
                return True
            else:
                bo[row][column] = 0

    return False
            
#valid checks if a number suits in the spot
def valid(bo, num, pos):
    #check each row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check each column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    #check each box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True

#find_empty finds the spot that needs to be filled
def find_empty(bo):
     
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i,j)

    return None


#testing
print_board(board)
solver(board)
print("---------------------")
print_board(board)
