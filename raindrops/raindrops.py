def convert(number):
    drops = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    speak = [s for n, s in drops if number % n == 0]

    return "".join(speak) if speak else str(number)