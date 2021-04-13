
"""Random names generator."""


import sys
import random
from time import sleep
from collections import deque

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
         "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
         'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
         'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
         'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
         'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
         'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
         'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
         'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
         'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
         'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
         "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
         'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
         'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
         "Winston 'Jazz Hands'", 'Worms')

middle = ('_Appleyard', '_Bigmeat', '_Bloominshine', '_Boogerbottom',
        '_Breedslovetrout', '_Butterbaugh', '_Clovenhoof', '_Clutterbuck',
        '_Cocktoasten', '_Endicott', '_Fewhairs', '_Gooberdapple', '_Goodensmith',
        '_Goodpasture', '_Guster', '_Henderson', '_Hooperbag', '_Hoosenater',
        '_Hootkins', '_Jefferson', '_Jenkins', '_Jingley-Schmidt', '_Johnson',
        '_Kingfish', '_Listenbee', "_M'Bembo", '_McFadden', '_Moonshine', '_Nettles',
        '_Noseworthy', '_Olivetti', '_Outerbridge', '_Overpeck', '_Overturf')

last = ('Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')


def main():
    """Program generating funny names."""
    quit_msg = 'q'

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        middle_name = None
        if random.choice([True, False, False]):
            middle_name = random.choice(middle)

        name_sequence = [first_name]

        if middle_name is not None:
            name_sequence.append(middle_name)

        name_sequence.append(last_name)

        print(" ".join(name_sequence), file=sys.stderr)

        sleep(0.2)
        user_msg = input(
            f"Press {quit_msg} to finish, press 'Enter' to continue"
            f" the program:")

        if user_msg.lower() == quit_msg:
            break


if __name__ == '__main__':
    main()
