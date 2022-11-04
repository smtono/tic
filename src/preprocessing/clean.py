"""
This module is used to define functions used in cleaning the data.
Cleaning the data takes place in the following steps:
    - Restructuring data to conform to the format required by the model.
    - Adding toxicity metrics by running data through Perspective
    - Adding other sentiment metrics by running data through other libs
    - Using classifiers to classify the data into different categories
    - Dividing data into clusters by community
"""

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def demoji(text: str) -> str:
    """
    Executes the command

    Args:
        text (str):
            The text to remove emojis from
    Returns:
        The text with emojis removed
    """
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U00010000-\U0010ffff"
        "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', text)

def deurl(text: str) -> None:
    """
    Executes the command

    Args:
        args (list):
            The arguments to execute the command with
    Returns:
        None
    """
    url_pattern = re.compile(r"http\S+")
    return url_pattern.sub(r'', text)
    
def deretweet(text):
    """
    Uses regular expression to remove retweets from tweets

    Args:
        text (str):
            The string of text to be processed.
    Returns:
        The string of text with retweets removed.
    """
    return re.sub(r'^RT:[\r\n]*', '', text, flags=re.MULTILINE)

def remove_stopwords(text: str) -> str:
    """
    Removes stop words from the text

    Args:
        text (str):
            The text to remove stop words from
    Returns:
        The text with stop words removed
    """
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    return ' '.join(filtered_sentence)

def run_all(text: str) -> str:
    """
    Runs all of the cleaning functions on the text

    Args:
        text (str):
            The text to clean
    Returns:
        The cleaned text
    """
    text = demoji(text)
    text = deurl(text)
    text = deretweet(text)
    text = remove_stopwords(text)
    return text

if __name__ == "__main__":
    test = [
        "Hello, world!",
        "Hello, world! 😃",
        "Hello, world! 😃 https://www.google.com",
        "RT: Hello, world! 😃 https://www.google.com",
        "The quick brown fox jumps over the lazy dog"
        "and then the dog jumps over the fox"
        "but the fox is lazy and the dog is quick"
    ]
    
    for t in test:
        print(f"BEFORE: {t}")
        print(f"AFTER: {run_all(t)}")
