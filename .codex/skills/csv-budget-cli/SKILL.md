# CSV Budget CLI Skill

## When To Use
Use this skill when working on the repository's CSV-based budget CLI features, tests, refactors, or quality checks.

## Core Workflow
1. Write tests first.
2. Implement the smallest change that satisfies them.
3. Run `pytest`.
4. Run `radon cc`.
5. Ask `qa_engineer` to review the change before committing.

## Quality Checklist
- All public functions must have type hints.
- Keep functions short and focused.
- Keep cyclomatic complexity at 10 or below.
- Preserve CSV input/output behavior.

## Notes
This skill exists to keep the project workflow consistent for future Codex sessions.
