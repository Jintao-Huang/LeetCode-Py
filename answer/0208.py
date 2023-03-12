from leetcode_alg import *
_Trie = Trie


class Trie:
    def __init__(self):
        self.trie = _Trie()

    def insert(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        tn = self.trie.search(word)
        return bool(tn and tn.finish)

    def startsWith(self, prefix: str) -> bool:
        tn = self.trie.search(prefix)
        return bool(tn)


if __name__ == "__main__":
    callable_list = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    args_list = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    y = call_callable_list(callable_list, args_list, globals())
    assert y[1:] == [None, True, False, True, None, True]
