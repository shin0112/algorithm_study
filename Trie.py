# 동적 문자열을 저장하는 트리 형태의 데이터 구조(영어사전)
# 각 노드는 단일 문자를 나타내며 각 에지는 각 문자의 단어
# 마지막 문자에 bool값을 지정해 단어의 유무를 확인하게 함
# 자식 노드가 없으면 지워도 되고, 자식 노드가 있으면 bool값만 수정해줘야 함

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]

        return node.is_end_of_word
    
    def delete(self, word):
        node = self.root
        if self.search(word):
            for i in range(len(word)):
                node = node.children[word[i]]
            node.is_end_of_word = False


trie = Trie()
words_insert = ["apple","app","hello","he","hell"]
words_search = ["apple","app","a","hello","he","hell"]

print("apple, app, hello, he, hell 삽입")
for word in words_insert:
    trie.insert(word)

print("apple, app, a, hello, he, hell 탐색\n")
for word in words_search:
    if trie.search(word) == True:
        print("\"{}\" Trie에 존재 O".format(word))
    else:
        print("\"{}\" Trie에 존재 X".format(word))


print()
print("hello 삭제\n")
trie.delete("hello")

if trie.search("hello"):
    print("\"hello\" Trie에 존재 O")
else:
    print("\"hello\" Trie에 존재 X")

