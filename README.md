# left-factoring
Left factoring is a grammar transformation technique that is useful for producing 
a grammar suitable for top-down parsing

# Key idea

The key of algorithm is that, for each non-terminal, we are going 
to find the longest common prefix of two or more productions

The Trie is very useful to find longest common prefix for set of words. 
So I use the trie as a basic data structure here.

# How to use

```
from  leftfactoring import  leftFactoring

leftFactoring("./production")
```

# Example of transformation

Input grammar  as follows

```
S->aEbS|iEtSbS|a |abbE | abcE
E->bE
```

Output grammar as follows after transformation

```
S->iEtSbS|aC
A->cE|bE
C->e|bA|EbS
E->bE
```

