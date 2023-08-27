class Solution:
    def rotate_old(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        elements =[]
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                #val is the term i,j are the old index
                val = matrix[i][j]
                #calculating new Index I,J
                I = j #new I is the old J
                J = n-i-1 #refer to the calculations on onenote
                #we will add val,I,J to a tuple and add that tuple to the elements list
                elements.append((val,I,J))
        
        #now look at the value for each element in the elements list and place it at its new Index
        for element in elements:
            val,I,J = element
            matrix[I][J] = val
    
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            #i keep tracks of rows 
            for j in range(i,n):# if you iterate from 0 to n you'll end up swapping each element twice, a set pf i,j value should only come ones
                #j keeps track of columns
                #generate a transponse of the matrix
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        #reversing each row
        for i in range(n):
            matrix[i].reverse()


                

if __name__ == "__main__":
    s=Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    excepted_output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    s.rotate(matrix)
    assert matrix == excepted_output