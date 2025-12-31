# Lab 1 Scoring Rubric

| Category | 1: Beginning | 2: Proficient | 3: Exemplary |
| :--- | :--- | :--- | :--- |
| **Project Structure** | Flat files; no folders or package `__init__.py`. | Used folders, but imports are messy or not using relative paths. | Professional structure with `docs/`, `school/`, and `main.py`. |
| **SOLID: SRP** | Classes handle their own data, logic, and printing. | Mostly separated, but models contain too much execution logic. | **Strict SRP:** Models define data; `main.py` handles execution. |
| **SOLID: OCP/ISP** | Research method is in the base class (Polluted interface). | Used a Mixin, but logic in `main` is hardcoded to class names. | **Interface/Mixin:** Loop uses `isinstance(Mixin)` for extension safety. |
| **Pythonic Implementation** | No `__str__` method or uses Java-style syntax. | Uses `__str__` and f-strings, but lacks type hints. | Uses type hints, dunder methods, and absolute/relative imports. |
| **Data Integrity** | No validation; allows grades outside 0-16. | Basic validation exists but is located outside the class. | **Encapsulation:** Class `__init__` enforces the 0-16 grade rule. |