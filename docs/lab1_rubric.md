# Lab 1 Scoring Rubric


| Requirement | 1: Beginning | 2: Proficient | 3: Exemplary |
| :--- | :--- | :--- | :--- |
| **Data Integrity** | Grade validation is missing; values over 16 allowed. | Validation exists but is a separate function or in `main.py`. | **Encapsulation:** Grade check (0-16) is strictly enforced inside the Class `__init__`. |
| **Attendance Logic** | Methods are missing or print identical messages. | Methods are overridden, but logic is hardcoded or repetitive. | **Polymorphism:** Methods are overridden in subclasses with distinct, requirement-specific messages. |
| **Research Capability** | `do_research` is in the base class (violates Interface Segregation). | Uses a Mixin, but the loop checks for the specific `CollegeStudent` class name. | **Composition:** Uses `ResearcherMixin` via multiple inheritance; loop checks for the Mixin type/capability. |
| **Project Layout** | All code is in a single `.py` file. | Files are split into modules, but logic is mixed or imports are not using package syntax. | **Modular:** Professional structure with separate files for protocols, subclasses, and a clean `main.py` entry point. |
| **Student Population** | Students are manually created one by one in the global scope. | Function exists to create students, but lacks grade variety or logic-based assignment. | **Dynamic:** Logic-driven population generates a diverse list of 6+ students programmatically. ||