# Truck allocation

The problem to be solved supposes the following statement (extracted from [here](https://johomo.hashnode.dev/abstractmodel-concretemodel-dataportal-and-problem-dumps-with-pyomo)):

We run a generalist product supplier business that sells a variety of products worldwide.
Every day a truck comes to the warehouse to load the items that must be delivered to 
retailers. Usually, the number total number of items to be shipped exceed truck's capacity.
Therefore, we must decide which items we load into the truck and which items stay on the 
warehouse until the next truck.

## Installation

- Base enviornment: You should have installed Python and pip.
- Miniconda (or Conda): It provides the most straightforward installation of the solver, already compiled. Check out [this](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#term-Miniconda) page.


## Development tools

- Type checking with flake8:
```bash
$ flake8 --max-line-length=89
```

## Running
```bash
$ python main.py
```

## Code structure
- `main.py`: Main execution file. It orchestrates the execution.
- `model.py`: Model definition and construction.
- `solver.py`: Defines the solver and its functions.
- `concrete_model_dump.txt`: Internal structure of the model (for debugging)
- `conda-env.yml`: Environment for Conda/Miniconda.
- `requirements.txt`: Requirements of the project.

## Attributions
- Base of the code and ideas extracted from _Josep's blog_ [here](https://johomo.hashnode.dev/abstractmodel-concretemodel-dataportal-and-problem-dumps-with-pyomo).
