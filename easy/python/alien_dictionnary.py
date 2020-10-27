"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographicaly in this alien language.
Excample:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    
Explanation:
    Build a transform mapping from order,
    Find all alien words with letters in normal order.

    For example, if we have order = "xyz..."
    We can map the word "xyz" to "abc" or "123"

    Then we check if all words are in sorted order.
"""
class Solution:
    # Optimised solution from discussions, not mine             
    def isAlienSorted(self, words, order):
        # Creating mapping of value: order.index(value)
        m = {c: i for i, c in enumerate(order)}
        # Get character c's index i from the mapping m
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))