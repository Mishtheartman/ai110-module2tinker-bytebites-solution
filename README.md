# ByteBites — Solution

This is the **reference solution** for the AI110 Module 2 Tinker *ByteBites*. Unlike the other
Tinkers, ByteBites has **no starter repo** — students build the whole workspace from scratch. This
repo is the finished workspace so you can compare your design and code against a complete example.
It is one reasonable solution, not the only correct one.

## What's here

| File | What it is |
|------|-----------|
| `bytebites_spec.md` | The client feature request + the four candidate classes (Part 1b). |
| `draft_from_copilot.md` | The messy first AI diagram, kept to show what the custom agent fixes (Part 1c). **Intentionally wrong.** |
| `bytebites_design.md` | The verified UML class diagram — the real design deliverable (Part 1e). |
| `CLAUDE.md` | The custom "design agent" that encodes house rules so the AI stays on-spec (Part 1d). |
| `ByteBites_Design_Reference.md` | The provided reference file with its Behavioral Instructions filled in. |
| `models.py` | The four classes + the filter / sort / total methods (Parts 2–3). |
| `test_bytebites.py` | The pytest suite (Part 4). |

## Run it

```bash
pip install -r requirements.txt   # installs pytest
python models.py                  # runs the manual demo scenario
python -m pytest                  # runs the test suite
```

## The design in one breath

Four classes, related by **composition** (not inheritance):

- **Customer** has a `purchase_history` of **Order**s.
- **Order** contains **FoodItem**s and can `calculate_total()`.
- **Menu** contains **FoodItem**s and can `filter_by_category()` / `sort_by_popularity()`.
- **FoodItem** is a plain data object: `name`, `price`, `category`, `popularity_rating`.

## The point of the lab

The design comes first. The most valuable artifact is `bytebites_design.md`, committed *before* any
Python — and the contrast between `draft_from_copilot.md` (unconstrained AI) and the final design
(AI constrained by `CLAUDE.md`) is the lesson: **you are the architect who says "no" to scope creep
and inheritance-where-composition-belongs.** If your classes match the spec's four responsibilities,
use composition, and your tests actually fail when the code is broken, you've hit the objectives.
