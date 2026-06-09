def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError(f'{length} is a ValueError')
    return [series[i:i + length] for i in range(len(series) - length+1)]
