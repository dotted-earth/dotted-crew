# CONTRIBUTING

## Prerequisites

1. ensure you have a python manager [pyenv installed](https://github.com/pyenv/pyenv-installer)
2. create virtualenv `pyenv virtualenv dotted-crew`
3. activate venv `pyenv activate dotted-crew`
4. activate local venv `pyenv local dotted-crew`
5. ensure your in the correct venv `pyenv which pip` should output `/Users/your_username/.pyenv/versions/dotted-crew/bin/pip`
6. run `pip install`

## Start server

`uvicorn src.main:app --port 5500 --reload`

## Crew AI

1. [Docs](https://docs.crewai.com/core-concepts/Tasks/)
