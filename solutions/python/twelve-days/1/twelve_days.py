def recite(start_verse, end_verse):
    _COUNTING = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
                 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    _CONTENTS = ['a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens',
                 'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying',
                 'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing',
                 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']

    def first_part(verse):
        part_one = f"On the {_COUNTING[verse]} day of Christmas my true love gave to me: "
        return part_one

    def content_part(verse):
        part_two = ''
        if verse > 0:
            for verse in _CONTENTS[verse:0:-1]:
                part_two += verse + ', '
            return part_two + f"and {_CONTENTS[0]}."
        else:
            return part_two + f"{_CONTENTS[0]}."

    verses = list()
    for index in range(start_verse-1, end_verse):
        verses.append(first_part(index) + content_part(index))
    return verses
