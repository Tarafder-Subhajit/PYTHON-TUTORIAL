"""
A virtual environment is a self-contained Python environment that contains:

A specific Python interpreter
Project-specific Python packages
Independent package versions

Without a virtual environment, all Python packages are installed globally on the machine, which can lead to conflicts between projects.

Example Problem: Suppose,
Project A requires requests==2.28
Project B requires requests==2.32

If both are installed globally, one project may break.

A virtual environment solves this by keeping dependencies separate.

Lets explore devops usecases:

1. Dependency resolution

project1/
    venv/
    app.py

project2/
    venv/
    app.py

Both projects can use different package versions.


Create a virtual environment: python -m venv venv
Activate it: source venv/bin/activate
After activation, your prompt usually changes to: (venv)$

DEVOPS USE CASES:

1. CI/CD Pipeline Execution
        python -m venv venv

        source venv/bin/activate

        pip install -r requirements.txt

        pytest

"""