# test4.py
#
import sys, sudoku
from sideBySide import sideBySide

def test4 () :
    game = sudoku.Game(sys.argv[1])
    before = game.display()
    while game.iterate() : pass
    after = game.display()
    print "\n        Before                    After"
    print sideBySide([before,after])
    if game.valid() and not game.finished() :
        print "This partial yet valid game splits into"
        kids = game.split()
        print sideBySide([after]+map(lambda x: x.display(), kids))
    if not game.valid() :
        print "This game is not valid and cannot be completed"

if __name__ == "__main__" : test4()
