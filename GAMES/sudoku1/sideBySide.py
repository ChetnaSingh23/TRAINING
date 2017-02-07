# sideBySide.py
#
def sideBySide (blocks) :
    "concatenate multiple blocks of text horizontally"
    left  = blocks[0].split('\n')
    for right in blocks[1:] :
        right = right.split('\n')
        maxlen = max(len(left),len(right))
        if len(left)  < maxlen : left  += ['']*maxlen
        if len(right) < maxlen : right += ['']*maxlen
    
        left  = map(lambda x: x.strip(), left)
        right = map(lambda x: x.strip(), right)
    
        spread = max(map(lambda x: len(x), left)) + 4
        left   = map(lambda x: x.ljust(spread), left)
    
        out = []
        for i in range(maxlen) :
            out.append("  %s %s" % (left[i],right[i]))
        left = out
    return '\n'.join(left)

def test() :
    import sys
    files = sys.argv[1:]
    blocks = map(lambda fil: open(fil).read(), files)
    print sideBySide(blocks)

if __name__ == "__main__" : test()

