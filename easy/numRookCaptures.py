lass Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        
        #get rook position
        row,col=0,0
        for i,x in enumerate(board):
            for j,y in enumerate(x):
                
                if y == "R":
                    row = i
                    col = j
        
        count = 0
        
        #go up
        
        r,c = row,col
        while r>=0:
            
            if board[r][c] == "p":
                count+=1
                break
            
            if board[r][c] == "B":
                break
            
            r-=1
        
        #go down
        
        r,c = row,col
        while r<len(board):
            
            if board[r][c] == "p":
                count+=1
                break
            
            if board[r][c] == "B":
                break
            
            r+=1
        
        #go left
        r,c = row,col
        while c>=0:
            
            if board[r][c] == "p":
                count+=1
                break
            
            if board[r][c] == "B":
                break
            
            c-=1
        
        #go right
        r,c = row,col
        while c<len(board[r]):
            
            if board[r][c] == "p":
                count+=1
                break
            
            if board[r][c] == "B":
                break
            
            c+=1

        return count
