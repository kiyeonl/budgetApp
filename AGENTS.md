# Project Rules

## Project Overview
This repository is a Python CLI budget app that manages ledger data stored in CSV files.

## Coding Rules
- Type hints are required for all functions.
- Keep each function to 50 lines or fewer.

## TDD Rules
- Always write tests before implementation.

## Quality Rules
- Keep cyclomatic complexity at 10 or below.

## Quality Review Rules
- Before committing, always run quality review through the `qa_engineer` subagent.

## Test Commands
- `pytest`
- `radon cc`

## Commit Rules
- When one feature is complete, commit and push it.
