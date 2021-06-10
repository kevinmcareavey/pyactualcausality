def format_dict(data, sep_item=", ", sep_key_value="=", brackets=True):
    output = ""
    delim = ""
    for key, value in data.items():
        output += f"{delim}{key}{sep_key_value}{value}"
        delim = f"{sep_item}"
    return f"{{{output}}}" if brackets else f"{output}"


def powerdict(data):  # https://stackoverflow.com/a/1482320
    n = len(data)
    masks = [1 << i for i in range(n)]
    for i in range(1 << n):
        yield {key: data[key] for mask, key in zip(masks, data) if i & mask}


def powerset(data):  # https://stackoverflow.com/a/1482320
    n = len(data)
    masks = [1 << i for i in range(n)]
    for i in range(1 << n):
        yield {element for mask, element in zip(masks, data) if i & mask}
