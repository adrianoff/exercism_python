def recite(start_verse, end_verse):
    tmpl = 'On the %s day of Christmas my true love gave to me: %s.'
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

    for i, day in enumerate(days[start_verse-1:end_verse-1]):

        items_str = [item for item in items[:i]]

    pass
