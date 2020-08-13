def word_count(s):
    # Your code here
    ignore_chars = [
    '"',
     ':',
     ';',
     ',',
     '.',
     '-',
     '+', 
     '=',
     '/',
    #  '\',
     '|',
     '[', 
     ']',
     '{',
     '}',
     '(',
     ')', 
     '*',
     '^' 
     ]

    count_string = s.lower().split()
    table = {}

    for word in count_string:
        if word in table:
            table[word] += 1
        else:
            table[word] = 1 

    return table



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))