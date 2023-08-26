from collections import Counter

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #n=9 #it represents the number of rows and columns
        dict_row,dict_col={},{}
        for i in range(9):
            for j in range(9):
                #first make sure the element is not empty
                if board[i][j]!=".":
                    #now check of the value of i  is present in dict_row
                    if i in dict_row:
                        #that means we came across the row before, check if the value exists, if it does return false else add the value to the list
                        if board[i][j] in dict_row[i]:
                                return False
                        else:
                            dict_row[i].add(board[i][j])
                    else:
                        #the row is not present in the dict add it
                        dict_row[i] = set()       
                        dict_row[i].add(board[i][j])
                    #now check of the value of j  is present in dict_row
                    if j in dict_col:
                        #that means we came across the col before, check if the value exists, if it does return false else add the value to the list
                        if board[i][j] in dict_col[j]:
                            return False
                        else:
                            dict_col[j].add(board[i][j])   
                    else:
                        dict_col[j]=set()
                        dict_col[j].add(board[i][j])
        
        #if the code reaches this stage that means there are no duplicates in rows and columns
        #the dictionaries are no longer needed we can delete them
        del dict_col,dict_row
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                sub_squares = set()
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if board[x][y]!=".":
                            #check if the element is not empty 
                            #now check if  the element is in sub_squares
                            if board[x][y] in sub_squares:
                                #element already exists
                                return False
                            else:
                                #element not in visited set, add it to the set
                                sub_squares.add(board[x][y])
                
        return True

if __name__ == "__main__":
    s=Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))
    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))