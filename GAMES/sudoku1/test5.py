# test5.py
#
import sys, sudoku
from sideBySide import sideBySide

def test5 () :
    game = sudoku.Game(sys.argv[1])
    explore(game)

def explore (game) :
    before = game.display()
    while game.iterate() : pass
    after = game.display()
    if not game.valid() :
        print "\n        Before                    After   (Invalid)"
        print sideBySide([before,after])
        bad = [cell for cell in game.cells if cell.error > ""]
        print bad[0], bad[0].error
        return
    elif game.finished() :
        print "\n        Before                    After   (Finished)"
        print sideBySide([before,after])
        return
    else : 
        message = "Partial game splits"
        kids = game.split()
        displays = [kid.display() for kid in kids]
        print "\n        Before                    After   (Splits into .... )"
        print sideBySide([after]+displays)
        for kid in kids :
            explore(kid)

if __name__ == "__main__" : test5()
