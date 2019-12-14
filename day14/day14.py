from collections import namedtuple, defaultdict
import math

Formula = namedtuple('Formula', 'product reactants')
Product = namedtuple('Product', 'quantity name')
Reactant = namedtuple('Reactant', 'quantity name')


def find_reactants(formulas, need, produced, product='FUEL'):
    print(f'product: {product} need: {need} produced: {produced}')
    if product == 'ORE':
        return need
    else:
        formula = formulas[product]
        if produced[product] < need:
            multiplier = math.ceil(need / formula.product.quantity)
        else:
            multiplier = 0

        produced[product] += (multiplier * formula.product.quantity) - need

        needs = {reactant.name: multiplier * reactant.quantity for reactant in formula.reactants}

        return sum(find_reactants(formulas, needs[reactant.name], produced, reactant.name) for reactant in formula.reactants)


def main(filename="puzzle1.in"):
    with open(filename) as file:
        lines = file.read().splitlines()

    reactions = [line.split(' => ') for line in lines]
    reactions = [(reaction[1].split(' '), [reactant.split(' ') for reactant in reaction[0].split(', ')]) for reaction in reactions]

    formulas = {reaction[0][1]: Formula(product=Product(quantity=int(reaction[0][0]), name=reaction[0][1]), reactants=[Reactant(quantity=int(reactant[0]), name=reactant[1]) for reactant in reaction[1]]) for reaction in reactions}

    for key in formulas.keys():
        print(f'{key}: {formulas[key]}')

    produced = defaultdict(int)

    return find_reactants(formulas, 1, produced)


if __name__ == "__main__":
    print(main())
