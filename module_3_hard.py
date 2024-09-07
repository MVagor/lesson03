def calculate_structure_sum(data_str):
    all_sum=0
    if isinstance(data_str, (int, float)):
        return data_str
    elif isinstance(data_str, str):
        return len(data_str)
    elif isinstance(data_str, (tuple, list, set)):
        for num in data_str:
            all_sum += calculate_structure_sum(num)
    elif isinstance(data_str, dict):
        for key_dict, el_dict in data_str.items():
            all_sum += calculate_structure_sum(key_dict)
            all_sum += calculate_structure_sum(el_dict)
    return all_sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)