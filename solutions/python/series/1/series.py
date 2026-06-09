def slices(series, length):
    series_length = len(series)
    try:
        serie=int(series)
    except ValueError:
        return 'ValueError'
    if length < 1 or length > series_length:
        return 'ValueError'
    return list(series[number:number + length] for number in range(len(series) - length+1))
