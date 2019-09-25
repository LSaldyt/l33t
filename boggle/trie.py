class TrieNode:
    def __init__(self, set_radix=None):
        self.radix     = set_radix
        self.children  = dict()

    def add_character(self, c):
        self.children[c] = TrieNode(c)

    def add(self, s):
        current = self
        s += '*'
        for c in s:
            child = TrieNode(c)
            current.children[c] = child
            current = child

    def all(self):
        if self.radix == None:
            return [child.all() for child in self.children.values()]
        elif len(self.children) == 0:
            return [[self.radix]]
        return [[self.radix] + path for child in self.children.values() for path in child.all()]

    def __hash__(self):
        return hash(self.radix)

    def __str__(self):
        return '\n'.join(''.join(map(str, x)) for l in self.all() for x in l)

    def isword(self, item, prefix=False):
        current = self
        for c in item:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        if prefix or current.radix == '*':
            return True
        return False

    def __contains__(self, item):
        return self.isword(item)
