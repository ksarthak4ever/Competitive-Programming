# Autocomplete System

Design an autocomplete system with insert, search and startsWith methods.

```
Example :-
words = Autocomplete()
words.insert(“Sarthak”)
words.insert(“Kumar”)
words.search(“Sarthak”) // True
words.search(“Testing”) // False
words.startsWith(“Sart") // True
words.startsWith(“Test”) // False
```

## Solution 

The best data structure to implement the autocomplete system is a Trie.

The time and space complexity of insert are both linear.

The time complexity of search and startsWith is linear and the space complexity for both methods is constant.