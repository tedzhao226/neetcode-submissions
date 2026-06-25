class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # hashmaps
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {(r, c): set() for r in range(3) for c in range(3)}

        # nested loop thru
        for r, row in enumerate(board):
            for c, v in enumerate(row):
                
                if v in rows[r] or v in cols[c] or v in boxes[r // 3, c // 3]:
                    return False

                # dont forget to remove the placeholder
                if v != ".":
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[r // 3, c // 3].add(v)
        
        return True

