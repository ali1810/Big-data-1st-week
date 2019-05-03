def Matchex(text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (Matchex(text, pattern[2:]) or
                    first_match and Matchex(text[1:], pattern))
        else:
            return first_match and Matchex(text[1:], pattern[1:])
text = input('Enter First  string: ')
pattern = input('Enter second pattern with *(star) .(dot) and a to z string: ')
Matchex(text,pattern)
