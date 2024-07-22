def duplicate_values(my_dict):
    seen = set()
    duplicates = []
    values_seen = set()
    
    for key, value in my_dict.items():
        if value in values_seen:
            if value not in seen:
                duplicates.append(value)
                seen.add(value)
        else:
            values_seen.add(value)
    
    return duplicates

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3}
result = duplicate_values(my_dict)

print(result)
