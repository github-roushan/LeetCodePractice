
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from hashlib import md5
from typing import Dict, List

from sortedcontainers import SortedList


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass(order=True)
class Node:
    """A single folder in the directory tree."""

    # `order=True` lets ``SortedList`` keep nodes in lexicographic order based
    # on their folder names (`val`).  The remaining attributes are excluded
    # from the comparison so they do not affect the order.
    val: str
    children: SortedList = field(default_factory=SortedList, repr=False, compare=False)
    child_hash: str = field(default="", repr=False, compare=False)
    subtree_hash: str = field(default="", repr=False, compare=False)

    # A nice human-readable representation for debugging / logging.
    def __repr__(self) -> str:  # pragma: no cover – utility only
        return f"Node({self.val})"


class Trie:
    """Directory tree with helper methods for duplicate-subtree removal."""

    def __init__(self, root_val: str = "/") -> None:
        self.root: Node = Node(root_val)

    # ---------------------------------------------------------------------
    # Building the tree
    # ---------------------------------------------------------------------

    def insert(self, path: List[str]) -> None:
        """Insert a full folder *path* into the trie (iterative version)."""

        node = self.root
        for folder in path:
            node = self._get_or_create_child(node, folder)

    @staticmethod
    def _get_or_create_child(parent: Node, folder: str) -> Node:
        """Return an existing child folder or create it if missing."""

        for child in parent.children:
            if child.val == folder:
                return child

        new_child = Node(folder)
        parent.children.add(new_child)  # Sorted insert (O(log n))
        return new_child

    # ---------------------------------------------------------------------
    # Hash calculation (post-order traversal)
    # ---------------------------------------------------------------------

    def compute_hashes(self) -> Dict[str, int]:
        """Populate *child_hash* / *subtree_hash* and return frequency map."""

        freq: Dict[str, int] = defaultdict(int)

        # Non-recursive post-order traversal → each node is pushed twice.
        stack: List[tuple[Node, bool]] = [(self.root, False)]

        while stack:
            node, visited = stack.pop()

            if not visited:
                # First time we see the node → push it back as *visited* and
                # then process its children.
                stack.append((node, True))
                for child in reversed(node.children):  # reverse keeps order
                    stack.append((child, False))
                continue

            # ----------------------------------------------------------------
            # Children processed → compute hashes for *node*.
            # ----------------------------------------------------------------

            child_hashes = [child.subtree_hash for child in node.children]

            if child_hashes:
                joined = "|".join(child_hashes)
                node.child_hash = md5(joined.encode()).hexdigest()
                freq[node.child_hash] += 1

            # Now build the full subtree hash (children + own folder name).
            own_hash = md5(node.val.encode()).hexdigest()
            subtree_parts = child_hashes + [own_hash]

            if len(subtree_parts) == 1:
                node.subtree_hash = own_hash  # leaf folder
            else:
                joined = "|".join(subtree_parts)
                node.subtree_hash = md5(joined.encode()).hexdigest()

        return freq

    # ---------------------------------------------------------------------
    # Removing duplicate subtrees
    # ---------------------------------------------------------------------

    def remove_duplicates(self, freq: Dict[str, int]) -> None:
        """Prune child folders whose *child_hash* occurs more than once."""

        stack: List[Node] = [self.root]

        while stack:
            node = stack.pop()

            # Create a *snapshot* list because we may mutate *children*.
            for child in list(node.children):
                if child.child_hash and freq[child.child_hash] > 1:
                    node.children.remove(child)
                else:
                    stack.append(child)

    # ---------------------------------------------------------------------
    # Collecting remaining paths
    # ---------------------------------------------------------------------

    def collect_paths(self) -> List[List[str]]:
        """Return every path in the current trie (pre-order, iterative)."""

        result: List[List[str]] = []
        stack: List[tuple[Node, List[str]]] = [(self.root, [])]

        while stack:
            node, path_so_far = stack.pop()
            current_path = path_so_far + [node.val]

            # Skip the root “/” when adding to *result*.
            if path_so_far:  # not the root
                result.append(current_path[1:])

            # Pre-order: push children in *reverse* lexicographic order so that
            # the left-most (smallest) child is processed first when popped.
            for child in reversed(node.children):
                stack.append((child, current_path))

        return result


# ---------------------------------------------------------------------------
# Public API expected by LeetCode / callers
# ---------------------------------------------------------------------------


class Solution:
    """LeetCode solution wrapper (unchanged public signature)."""

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:  # noqa: N802 – LeetCode name
        trie = Trie("/")

        # 1. Build the directory tree.
        for path in paths:
            trie.insert(path)

        # 2. Compute hashes + frequency map.
        freq = trie.compute_hashes()

        # 3. Remove duplicates based on the frequency map.
        trie.remove_duplicates(freq)

        # 4. Collect and return the remaining paths.
        return trie.collect_paths()
