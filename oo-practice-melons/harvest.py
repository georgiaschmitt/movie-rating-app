############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    # fido = Animal('Fido')   # making an object ("instantiating")
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberry')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pair in melon.pairings:
            print(f'-{pair}')
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_dict = {}

    for melon in melon_types:
        melons_dict[melon.code] = melon

    return melons_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        return True if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != "Field 3" else False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, "Field 2", "Sheila")
    melon_2 = Melon(melons_by_id['yw'], 3, 4, "Field 2", "Sheila")
    melon_3 = Melon(melons_by_id['yw'], 9, 8, "Field 3", "Sheila")
    melon_4 = Melon(melons_by_id['cas'], 10, 6, "Field 35", "Sheila")
    melon_5 = Melon(melons_by_id['cren'], 8, 9, "Field 35", "Michael")
    melon_6 = Melon(melons_by_id['cren'], 8, 2, "Field 35", "Michael")
    melon_7 = Melon(melons_by_id['cren'], 2, 3, "Field 4", "Michael")
    melon_8 = Melon(melons_by_id['musk'], 6, 7, "Field 4", "Michael")
    melon_9 = Melon(melons_by_id['yw'], 7, 10, "Field 3", "Sheila")

    return [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        print(
            f"Harvested by {melon.harvested_by} from {melon.harvested_from} {'(CAN BE SOLD)' if melon.is_sellable() else '(NOT SELLABLE)'} ")


def create_melon_objects(filename):
    melon_object = []
    data = open(filename)
    for line in data:
        _, shape_rating, _, color_rating, _, code, _, _, harvested_by, * \
            harvested_from = line.rstrip().split(" ")
        shape_rating = int(shape_rating)
        color_rating = int(color_rating)
        harvested_from.remove('#')
        harvested_from = ' '.join(harvested_from)

        melon_by_id = make_melon_type_lookup(make_melon_types())
        melon = Melon(melon_by_id[code], shape_rating,
                      color_rating, harvested_from, harvested_by)
        melon_object.append(melon)
    data.close()

    return melon_object
