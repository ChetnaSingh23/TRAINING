import sys
from sudoku import Game, Cell
from sideBySide import sideBySide

def test2 () :
    "Set up a dual set and show effects"
    game = Game(sys.argv[1])
    tagged = game.getTagged()
    tags=tagged.keys(); tags.sort()
    before = game.display()
    for tag in tags :
        cell = tagged[tag]
        print " ", tag, cell, cell.pvals
        cell.update_pvals(game.cells)
        print " ", tag, cell, cell.pvals

    after = game.display()
    print "\n        Before                    After"
    print sideBySide([before,after])

if __name__ == "__main__" : test2()
