class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # nested loop thru
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {(r, c): set() for r in range(3) for c in range(3)}


        for r, row in enumerate(board):
            for c, v in enumerate(row):
                
                if v in rows[r] or v in cols[c] or v in boxes[r // 3, c // 3]:
                    return False

                if v != ".":
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[r // 3, c // 3].add(v)
        
        return True

