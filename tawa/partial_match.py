import difflib

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def partial_match(text, pattern, threshold=0.6):
    """
    Returns True if the similarity ratio between text and pattern is above threshold.
    """
    matcher = difflib.SequenceMatcher(None, text, pattern)
    return matcher.ratio() >= threshold

if __name__ == "__main__":
    filename = input("Enter the filename to read: ")
    pattern = input("Enter the pattern to search: ")
    text = read_file(filename)
    lines = text.splitlines()
    print("Lines with partial match:")
    for line in lines:
        if partial_match(line, pattern):
            print(line)