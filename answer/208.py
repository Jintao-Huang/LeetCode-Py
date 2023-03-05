from leetcode_alg import *
_Trie = Trie


class Trie:
    def __init__(self):
        self.trie = _Trie()

    def insert(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        tn = self.trie.search(word)
        return tn is not None and tn.finish

    def startsWith(self, prefix: str) -> bool:
        tn = self.trie.search(prefix)
        return tn is not None


if __name__ == "__main__":
    callable_list = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    args_list = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    print(call_callable_list(callable_list, args_list, globals()))
