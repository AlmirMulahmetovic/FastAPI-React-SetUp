def to_camel_case(snake_string):
    words = snake_string.split("_")
    return words[0] + "".join([word.title() for word in words[1:]])
