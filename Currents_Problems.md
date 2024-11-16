# ISSUES

## PIECES

### KING
- The king cannot castle through a check.

## FUNCTIONS
- There are moves that do nothing. (didn't reproduce, but clicks on pieces with no moves make it weird when clicking another piece right after)
- castling does not work. (the king moves 2 places but the rook doesn't move) (fixed itself(? ))
- Enpassant is not working again.
- Solve the problems with the checks
  and the castling with enpassant.
  (the problems are doing the movements but not undoing the states of the pieces. eg: self.not_moved and self.enpassant)
  
## GAME
- Solve performance issues
- Complete Fen string function

## READABILITY
- Improve the readability of the code and change comments.

## TESTING
- Create test to be sure that there are no moves against the rules.

