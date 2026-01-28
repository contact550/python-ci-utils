# My First CI/CD Project 🚀

![CI Status](https://github.com/contact550/python-ci-utils/actions/workflows/ci.yml/badge.svg)

# Data Processor CI/CD Project

A Python-based data processing application integrated with a multi-stage **GitHub Actions** pipeline. This project demonstrates automated testing, code quality enforcement, and artifact generation.

## 🚀 Features
* **Data Processing**: Functions for normalization, outlier filtering, and statistical analysis.
* **Automated Testing**: Robust test suite using `pytest` with parameterized test cases.
* **Linting**: Code style enforcement using `flake8` to maintain PEP 8 standards.
* **CI/CD Pipeline**: A fully automated workflow using GitHub Actions with job dependencies.

## 📁 Project Structure
* `src/processor.py` — Core logic and data processing functions.
* `tests/test_processor.py` — Automated tests and edge-case validations.
* `.github/workflows/ci.yml` — Multi-stage pipeline configuration.
* `requirements.txt` — Project dependencies (`pytest`, `flake8`).

## ⚙️ CI/CD Pipeline Workflow
The pipeline is designed with a "fail-fast" approach using the `needs` keyword:

1. **Tests**: Executes the test suite. If any test fails, the pipeline stops.
2. **Lint**: Checks code formatting and quality. Only runs if **Tests** pass.
3. **Report**: Generates a build summary and saves it as a downloadable **GitHub Artifact**.

## 🛠 Local Setup
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
