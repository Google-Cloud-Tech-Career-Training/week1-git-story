import words

story = f"""{words.name1} and {words.name2} went shopping for {words.pluralNoun1} in the city.
Everywhere they looked they saw {words.adjective1} signs and {words.adjective2} people.
{words.name1} saw a man selling {words.pluralNoun2} from a cart and decided to buy one
because {words.name2} was hungry. {words.name2} wanted to explore the {words.pluralNoun3} stores.
One store had a selection of {words.pluralNoun4} and {words.adjective3} {words.pluralNoun5}. A
shop owner brought out a {words.noun1} that {words.name2} liked but {words.name1} said it looked
too {words.adjective4}. At the next shop {words.name1} found the perfect {words.clothingItem1} but
noticed it was missing a {words.noun2}. Meanwhile, a {words.adjective5} {words.clothingItem2} fit
{words.name2} {words.adverb1}! After a long day of shopping they both rested their
{words.pluralBodyPart1} near a {words.adjective6} {words.noun3} by the busy sidewalk."""

def print_story():
    with open("story.txt", "w") as f:
        f.write(story)
    f.close()