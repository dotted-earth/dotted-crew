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
3. Start server: `uvicorn server:app --reload`
