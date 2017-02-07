import sys
from sudoku import Game, Cell
from sideBySide import sideBySide

def test1 () :
    "Set up a dual set and show effects"
    game = Game(sys.argv[1])
    before = game.display()
    tagged = game.getTagged()
    tags = tagged.keys(); tags.sort()
    for tag in tags :
        cell = tagged[tag]
        for other in game.cells :
            if other.inx in cell.sameRow : other.val="r"
            if other.inx in cell.sameCol : other.val="c"
            if other.inx in cell.sameBox : other.val="b"

    after = game.display()
    print sideBySide([before,after])

if __name__ == "__main__" : test1()
