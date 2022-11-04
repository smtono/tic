"""
This moudle is used to define functions used for analyzing text data
This text will be analyzed using natural language processing using NLTK

The following distance measure for pieces of text will be used:
    - Jaccard Distance
    - Levenshtein Distance
    - Cosine Similarity
    - Etc

These will analyze how close two pieces of text are to each other
"""

from nltk.metrics import distance

def jaccard_distance(text1: str, text2: str) -> float:
    """
    Calculates the Jaccard Distance between two pieces of text

    Args:
        text1 (str):
            The first piece of text to be compared
        text2 (str):
            The second piece of text to be compared
    Returns:
        The Jaccard Distance between the two pieces of text
    """
    # Tokenize the text
    text1 = set(text1.split())
    text2 = set(text2.split())

    # Calculate the Jaccard Distance
    return len(text1.intersection(text2)) / len(text1.union(text2))

def levenshtein_distance(text1: str, text2: str) -> int:
    """
    Returns the Levenshtein Distance between two pieces of text
    
    Notes:
        The Levenshtein Distance is the minimum number of edits required to
        convert one piece of text into another

    Args:
        text1 (str):
            The first piece of text to be compared
        text2 (str):
            The second piece of text to be compared
    Returns:
        The Levenshtein Distance between the two pieces of text
    """
    return distance.edit_distance(text1, text2)

def cosine_similarity(text1: str, text2: str) -> float:
    """
    Returns the Cosine Similarity between two pieces of text

    Args:
        text1 (str):
            The first piece of text to be compared
        text2 (str):
            The second piece of text to be compared
    Returns:
        The cosine similarity between the two pieces of text
    """
    # Tokenize the text
    text1 = set(text1.split())
    text2 = set(text2.split())

    # Calculate the cosine similarity
    return len(text1.intersection(text2)) / (len(text1) * len(text2)) ** 0.5
