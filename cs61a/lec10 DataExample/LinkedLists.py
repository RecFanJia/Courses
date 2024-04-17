class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def is_ordered(s):
    while s:
        if s.first > s.rest.first:
            return False
        s = s.rest
    return True

def is_ordered_rec(s):


def is_abs_orderded(s):
    while s:
        if abs(s.first) > abs(s.rest.first):
            return False
        s = s.rest
    return True

def merge_two_sorted(s, t):
    if s.rest == Link.empty:
        s.rest = t
    else:
        s.rest = Link(t.first, merge_two_sorted(s.rest, t.rest))
    