text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary
text_dict = {}
for char in text:
    key = char
    if char in text_dict:
        text_dict[char] += 1
    else:
        text_dict[char] = 1
print(text_dict)
    