from collections import namedtuple, defaultdict
import math

Formula = namedtuple('Formula', 'product reactants')
Product = namedtuple('Product', 'quantity name')
Reactant = namedtuple('Reactant', 'quantity name')


def debug(f):
    def wrapper(*args, **kwargs):
        print(f'args: {args[1:]} kwargs: {kwargs}')
        return f(*args, **kwargs)
    return wrapper


@debug
def find_reactants(formulas, extra_produced={}, requested_quantity=1, product='FUEL'):
    if product == 'ORE':
        return requested_quantity, extra_produced
    formula = formulas[product]

    needed_quantity = requested_quantity - extra_produced.get(product, 0)
    multiplier = math.ceil(needed_quantity / formula.product.quantity)
    print(f'multi {product}: {multiplier} = ceiling(({requested_quantity} - {extra_produced.get(product, 0)}) / {formula.product.quantity})')

    extra = (formula.product.quantity * multiplier) - needed_quantity
    print(f'extra {product}: {extra} = (({multiplier} * {formula.product.quantity}) - {needed_quantity})')
    if extra:
        extra_produced[product] = extra
    elif product in extra_produced:
        del extra_produced[product]

    results = []
    print(f'searching children of {product}: {", ".join(reactant.name for reactant in formula.reactants)}')
    for reactant in formula.reactants:
        reactant_requested_quantity = multiplier * reactant.quantity
        result, extra_produced = find_reactants(formulas, extra_produced.copy(), reactant_requested_quantity, reactant.name)
        results.append(result)

    print(f'results {product}: {sum(results)} = {" + ".join(str(r) for r in results)}')

    return sum(results), extra_produced








    # needs = [product]
    # # quantity = {product: needed_quantity}
    # quantity = defaultdict(int)
    # quantity[product] = needed_quantity
    # # extra = defaultdict(int)
    # extra = {}

    # while needs != ['ORE']:
    #     # print(f'{needs} {quantity} {extra}')
    #     need = needs.pop(0)

    #     if need == 'ORE':
    #         # needs.append(need)
    #         continue

    #     formula = formulas[need]
    #     multiplier = math.ceil((quantity[need] - extra.get(need, 0)) / formula.product.quantity)
    #     # print(f'multi: {multiplier} = ceiling(({quantity[need]} - {extra.get(need, 0)}) / {formula.product.quantity})')

    #     excess_produced = (multiplier * formula.product.quantity) - quantity[need]
    #     if excess_produced:
    #         extra[need] = excess_produced
    #     # print(f'extra: {extra[need] if need in extra else None} = (({multiplier} * {formula.product.quantity}) - {quantity[need]})')

    #     for reactant in formula.reactants:
    #         quantity[reactant.name] += (multiplier * reactant.quantity) - extra.get(reactant.name, 0)
    #         if reactant.name not in needs:
    #             needs.append(reactant.name)

    #     del quantity[need]

    # return quantity[needs[0]]

    # print(f'product: {product} need: {need} produced: {produced}')
    # if product == 'ORE':
    #     return need
    # else:
    #     formula = formulas[product]
    #     if extra_produced[product] < need:
    #         multiplier = math.ceil(need / formula.product.quantity)
    #     else:
    #         return 0

    #     extra_produced[product] += (multiplier * formula.product.quantity) - need

    #     needs = {reactant.name: multiplier * reactant.quantity for reactant in formula.reactants}

    #     print(f'consume {", ".join(f"{v} {k}" for k,v in needs.items())} to produce {need} {product} with {extra_produced[product]} extra')

    #     return sum(find_reactants(formulas, needs[reactant.name], extra_produced, reactant.name) for reactant in formula.reactants)


def main(filename="puzzle1.in"):
    with open(filename) as file:
        lines = file.read().splitlines()

    reactions = [line.split(' => ') for line in lines]
    reactions = [(reaction[1].split(' '), [reactant.split(' ') for reactant in reaction[0].split(', ')]) for reaction in reactions]

    formulas = {reaction[0][1]: Formula(product=Product(quantity=int(reaction[0][0]), name=reaction[0][1]), reactants=[Reactant(quantity=int(reactant[0]), name=reactant[1]) for reactant in reaction[1]]) for reaction in reactions}

    # for key in formulas.keys():
    #     print(f'{key}: {formulas[key]}')

    # produced = defaultdict(int)

    return find_reactants(formulas)[0]


if __name__ == "__main__":
    print(main())
    # print(main('example1.in'))
