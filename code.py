#!/bin/python3

import os
from collections import defaultdict


class Node:
    def __init__(self, value: int):
        self.val: int = value
        self.children: list[Node] = []
        self.ancestors: set[Node] = set()
        self._total: int = 0
        self._parent: Node | None = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if self._parent:
            raise ValueError("Already have assigned a parent.")
        self.remove_child(parent)
        self.ancestors.add(parent)
        self._parent = parent

    def claim_family(self, ancestors: set = None):
        self.ancestors.update(ancestors or [])
        for child in self.children:
            child.parent = self
            child.claim_family(self.ancestors)

    def remove_child(self, child):
        initial_size = len(self.children)
        self.children = [c for c in self.children if c is not child]
        if len(self.children) != initial_size:
            self._total = 0  # Resets to calculate self.total on next access

    @property
    def total(self) -> int:
        if not self._total:
            self._total = self.val + sum((child.total for child in self.children), 0)
        return self._total

    def unrelated(self, other):
        return self not in other and other not in self

    def __contains__(self, other):
        """Is 'other' an ancestor of node (self) Called to evaluate: 'other in node' """
        if not isinstance(other, Node):
            return NotImplemented
        return other in self.ancestors


def balancedForest(vals, edges):
    nodes = [None] + [Node(val) for val in vals]
    for (parent, child) in edges:
        p, c = nodes[parent], nodes[child]
        p.children.append(c)
        c.children.append(p)
    root = nodes[1]
    root.claim_family()
    options: set[int] = set()
    seen: dict[int, list[Node]] = defaultdict(list)
    stack = root.children[:]
    n = root.total
    while stack:
        curr = stack.pop()
        stack.extend(curr.children)
        c = curr.total
        # Check for pairs not sharing a (non-root) ancestor
        if 0 <= (target := 3 * c - n) and seen[c]:
            options.add(target)
        if (oth := n - 2 * c) < c and any(curr.unrelated(t) for t in seen[oth]):
            options.add(c - oth)
        if c < (oth := (n - c) / 2) and any(curr.unrelated(t) for t in seen[oth]):
            options.add(int(oth) - c)
        seen[c].append(curr)
        # Check for ancestor options
        for old in curr.ancestors:
            a, b = n - old.total, old.total - c
            if a == b and c < b:
                options.add(b - c)
            if a == c and b < c:
                options.add(c - b)
            if b == c and a < c:
                options.add(c - a)
    return min(options, default=-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        vals = list(map(int, input().rstrip().split()))
        edges = []
        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))
        result = balancedForest(vals, edges)
        fptr.write(str(result) + '\n')
    fptr.close()
