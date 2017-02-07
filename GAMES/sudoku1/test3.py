# test3.py
#  update all iteractively until no changes happen
import sys, sudoku
from sideBySide import sideBySide

def test3 () :
    game = sudoku.Game(sys.argv[1])
    before = game.display()
    for iter in range(10) :
        changed = error = False
        for cell in game.cells[:] :
            earlier = cell.pvals.copy()
            if not cell.update_pvals(game.cells) :
                print cell, cell.error
                error = True
                break
            if cell.pvals != earlier :
                changed = True
        if not changed : break
        after = game.display()
        print "  Iteration", iter+1
        print "\n        Before                    After"
        print sideBySide([before,after])
        before = after
        if error : break

if __name__ == "__main__" : test3()
