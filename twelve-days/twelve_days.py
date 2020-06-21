def recite(start_verse, end_verse):
    firstline = 'On the %s day of Christmas my true love gave to me: '
    days = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth'
    ]

    items = [
        'a Partridge in a Pear Tree',
        'two Turtle Doves',
        'three French Hens',
        'four Calling Birds',
        'five Gold Rings',
        'six Geese-a-Laying',
        'seven Swans-a-Swimming',
        'eight Maids-a-Milking',
        'nine Ladies Dancing',
        'ten Lords-a-Leaping',
        'eleven Pipers Piping',
        'twelve Drummers Drumming',
    ]

    song = [firstline % days[start_verse-1]]

    for i in range(start_verse-1, -1, -1):
        song.append(items[i] + ', ')

    return song
