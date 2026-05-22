def flatten(iterable):
    final = []
    for obj in iterable:
        if isinstance(obj, list):
            final.extend(flatten(obj))
        elif obj is not None:
            final.append(obj)      
    return final