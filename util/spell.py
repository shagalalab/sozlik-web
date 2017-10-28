# Spellchecker is based on implementation by
# Peter Norvig at http://norvig.com/spell-correct.html
from collections import Counter


WORDS = None


def candidates(word, all_words):
    """Generate possible spelling corrections for word."""
    global WORDS
    WORDS = Counter(all_words)
    return known([word]) or known(edits1(word)) or known(edits2(word))


def known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    return set(w for w in words if w in WORDS)


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'aábcdefgǵhiıjklmnńoópqrstuúvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """All edits that are two edits away from `word`."""
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
