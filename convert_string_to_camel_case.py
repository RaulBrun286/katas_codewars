def to_camel_case(text):
    if not text:
        return ""
    words = text.replace("-", "_").split("_")
    return words[0] + "".join(p.capitalize() for p in words[1:])
