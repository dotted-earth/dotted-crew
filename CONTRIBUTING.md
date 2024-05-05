Install pipx
`brew install pipx`

## Prerequisites

1. Install pipx, `brew install pipx`
2. Install poetry, `pipx install poetry`
   - verify poetry install `poetry --version`

## Install dependencies

1. `poetry install --no-root`

## Start

1. View env created from install `poetry env list`
2. Enter poetry shell python env, `poetry shell`
3. Start server: `uvicorn src.main:app --port 5500 --reload`

## Crew AI

1. [Docs](https://docs.crewai.com/core-concepts/Tasks/)
