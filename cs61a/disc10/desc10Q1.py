"""
>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))

>>> Pair('and', Pair(Pair('<', Pair(1, Pair(0, nil))), Pair(Pair('/', Pair(1, Pair(0, nil))), nil)))
( and ( < 1 0) (/ 1 0))

# Discussion Time: What does (and (< 1 0) (/ 1 0)) evaluate to? 
False """