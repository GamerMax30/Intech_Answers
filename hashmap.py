def hashmap(values):
    buckets = dict()  # initialization of empty dict

    for value in values:
        # index calculation by taking hash value modulo size
        index = hash(value) % 10
        if index in buckets:
            buckets[index].append(value)
        else:
            buckets[index] = [value]
    return buckets


values = range(100)  # generate range of 100 values
mapped = hashmap(values)  # mapping values to buckets

for index, record in mapped.items():
    print(f"Bucket {index}: {record}")
