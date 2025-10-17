# engine-python 🐍

This repository is a simple showcase of how to **build a Python project using [engine-ci](https://github.com/containifyci/engine-ci)**.  

---

## What’s Inside

- Example **Python FlaskAPI project** (`app.py`)
- Minimal **Engine-CI pipeline** definition (`.containifyci`)
- Ready-to-run build steps for testing and packaging

---

## Quick Start

### 1. Install Engine-CI

```bash
go install github.com/containifyci/engine-ci@latest
```

### 2. Build the Project

Run the following command from the repository root:

```bash
engine-ci run
```

This will:

* Run the Python build/test pipeline defined by engine-ci

---

## Learn More

* [engine-ci GitHub Repository](https://github.com/containifyci/engine-ci)
* [engine-ci Medium Blog Post](https://medium.com/@frank.ittermann_46267/part-3-engine-ci-the-simple-ci-cd-solution-that-actually-works-0632a6b0b125)

---
