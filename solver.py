import itertools
from typing import Optional

from pyomo.environ import ConcreteModel, SolverFactory, SolverStatus, value
from pyomo.opt.results import SolverResults


class Solver:
    def __init__(self, concrete_model: ConcreteModel):
        self.concrete_model: ConcreteModel = concrete_model
        self._solution: Optional[SolverResults] = None

    def solve(self) -> None:
        solver = SolverFactory('scip')
        self._solution = solver.solve(self.concrete_model, tee=True)

    def solution_exists(self) -> bool:
        solution_found = (
            self._solution.solver.status == SolverStatus.ok or
            self._solution.solver.status == SolverStatus.warning
        )
        return solution_found

    def print_solution(self) -> None:
        assert self.solution_exists(), 'The solver did not find any solution!'

        profits = value(self.concrete_model.objective_function)
        print(profits)
        print(f'Total profits: {profits} €')

        for product in self.concrete_model.products:
            number_of_items = (
                round(value(self.concrete_model.number_of_items[product]))
            )
            volume_item = self.concrete_model.volume[product]
            volume_product = number_of_items * volume_item
            print(
                f'{product}: '
                f'Put {number_of_items} items (this is {volume_product} m3.)'
            )
