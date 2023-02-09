def validate_sudoku(board):
    table = []
    accu = 0
    for i in range(9):
        table = []
        accu = 0
        for j in range(9):
            if(board[i][j]==0):
                return False
            table.add(board[i][j]) 
            accu+=board[i][j]
            
        if(accu!=45 & len(table)!=9):
            return False   
        
    for j in range(9):
            table = []
            accu =0
            for i in range(9): 
                if(board[j][i]):
                    return False
                table.add([j][i])
                accu+=board[j][i]
                
            if(accu!=45 & len(table)!=9):
                return False        
   
    for x in range(9):
        table=[]
        accu=0
    for y in range(9):
        