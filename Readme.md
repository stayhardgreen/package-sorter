# Package Sorter

This project implements a package-sorting function for a robotic automation system.

## Rules
- Packages are **bulky** if volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm.
- Packages are **heavy** if mass ≥ 20 kg.
- Dispatch results:
  - STANDARD: not bulky and not heavy
  - SPECIAL: bulky or heavy
  - REJECTED: bulky and heavy

## Run Tests

```bash
pip install -r requirements.txt
pytest
