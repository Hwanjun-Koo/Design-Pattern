
data_str = 'apple,beer,rice,chicken\n'
data_str += 'apple,beer,rice\n'
data_str += 'apple,beer\n'
data_str += 'apple,mango\n'
data_str += 'milk,beer,rice,chicken\n'
data_str += 'milk,beer,rice\n'
data_str += 'milk,beer\n'
data_str += 'milk,mango'

def gen_record(data_str):
    for line in data_str.strip().split('\n'):
        yield sorted(list(set(line.split(','))))
test = gen_record(data_str)
print(sorted(next(test)))
print(sorted(next(test)))

def gen_frequent_1_itemset(dataset,min_support):
    freq = {}
    for data in dataset:
        for item in data:
            freq[item] = freq.get(item, 0) + 1
    num_items = len(dataset)
    freq_1_items = (item for item, count in freq.items() if (count / num_items) >= min_support)
    return set(freq_1_items)
    
dataset = list(gen_record(data_str))
print(sorted(list(gen_frequent_1_itemset(dataset, 0.7))))

def gen_frequent_2_itemset(dataset,min_support):
    freq = {}
    for data in dataset:
        for item in data:
            freq[item] = freq.get(item, 0) + 1
    num_items = len(dataset)
    freqitemA = (item for item, count in freq.items() if (count / num_items) >= min_support)
    freqitemB = (item for item, count in freq.items() if (count / num_items) >= min_support)
    freq_2_items = set()
    return set(freq_2_items)
dataset = list(gen_record(data_str))
print(sorted(list(gen_frequent_2_itemset(dataset, 0.5))))
