
class TrieNode:
    def __init__(self, set_radix=None):
        self.radix     = set_radix
        self.children = set()

    def add_character(self, c):
        self.children.add(TrieNode(c))

    def add(self, s):
        current = self
        for c in s:
            child = TrieNode(c)
            current.children.add(child)
            current = child

    def all(self):
        if self.radix == None:
            return [child.all() for child in self.children]
        elif len(self.children) == 0:
            return [[self.radix]]
        return [[self.radix] + path for child in self.children for path in child.all()]

    def __hash__(self):
        return hash(self.radix)

    def __str__(self):
        return '\n'.join(''.join(map(str, x)) for l in self.all() for x in l)
