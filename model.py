from itertools import product

from pyomo.environ import (
    AbstractModel,
    Binary,
    Constraint,
    maximize,
    NonNegativeIntegers,
    NonNegativeReals,
    Objective,
    Param,
    Set,
    Var,
)
from pyomo.core.expr.numeric_expr import LinearExpression
from pyomo.core.expr.relational_expr import EqualityExpression, InequalityExpression


def get_abstract_model() -> AbstractModel:
    model = AbstractModel(name='truck')

    # Sets
    model.products = Set(
        name='products',
        doc='Products that can be load into the truck.',
    )

    # Parameters
    model.stock = Param(
        model.products,
        name='stock',
        doc='Total items requested for each product.',
        domain=NonNegativeIntegers,
    )

    model.profits = Param(
        model.products,
        name='profits',
        doc='Profits obtained for each product [€/item].',
        domain=NonNegativeReals,
    )

    model.volume = Param(
        model.products,
        name='volume',
        doc='Volume that occupies each product [m3].',
        domain=NonNegativeReals,
    )

    model.truck_volume = Param(
        name='truck_volume',
        doc='Volume capacity of the truck [m3].',
        domain=NonNegativeReals,
    )

    # Variables
    model.number_of_items = Var(
        model.products,
        name='number_of_items',
        doc='Number of each item to load into the truck.',
        domain=NonNegativeIntegers,
        bounds=number_of_items_bounds,
    )

    # Constraints
    model.volume_of_items_cannot_exceed_truck_volume = Constraint(
        name='volume_of_items_cannot_exceed_truck_volume',
        doc=volume_of_items_cannot_exceed_truck_volume.__doc__,
        rule=volume_of_items_cannot_exceed_truck_volume,
    )

    # Objective
    model.objective_function = Objective(
        rule=compute_profits,
        sense=maximize,
    )

    return model


# Auxiliar functions for variables
def number_of_items_bounds(
    model: AbstractModel,
    product: str,
) -> [int, int]:
    """Get lower and upper bound of number_of_items variable."""
    lower_bound = 0
    """if product == 'locker':      # Forcing minimum number of lockers.
        lower_bound = 2"""
    upper_bound = model.stock[product]
    return lower_bound, upper_bound


# Constraints
def volume_of_items_cannot_exceed_truck_volume(
    model: AbstractModel,
) -> InequalityExpression:
    """The volume of all the items cannot exceed the volume of the truck."""
    volume_items = sum(
        model.number_of_items[product] * model.volume[product]
        for product in model.products
    )
    return volume_items <= model.truck_volume


# Objective
def compute_profits(
    model: AbstractModel,
) -> LinearExpression:
    """Total of profits earned with the truck allocation."""
    profits = sum(
        model.number_of_items[product] * model.profits[product]
        for product in model.products
    )
    return profits
