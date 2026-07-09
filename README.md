# 🛡️ PYDANTIC — Learning Notes & Practice

A structured collection of **Pydantic V2 notes, concepts, and practical code examples**.

This repository documents my journey of learning Pydantic step by step, from basic data validation to complex models, custom validators, serialization, configuration, and real-world applications.

---

## 📌 About Pydantic

Pydantic is a Python library for **data validation and parsing using Python type hints**.

It helps developers:

* Validate incoming data
* Convert compatible data types automatically
* Create structured data models
* Apply field-level validation rules
* Validate nested and complex data
* Create custom validation logic
* Serialize models into dictionaries and JSON
* Generate clear validation errors

Pydantic is widely used in:

* FastAPI applications
* AI and LLM applications
* Backend development
* Data pipelines
* Configuration management
* API request and response validation
* Automation scripts

---

## 📚 Learning Roadmap

This repository is divided into 12 sections:

### ✅ Section 1 — Why Pydantic Exists

Topics covered:

* What is Pydantic?
* Why data validation is important
* Runtime validation
* Data parsing
* Type coercion
* ValidationError
* Pydantic beyond FastAPI
* Pydantic in AI applications

---

### ✅ Section 2 — Building Your First Model

Topics covered:

* `BaseModel`
* Creating models
* Required fields
* Optional fields
* Default values
* Nullable fields
* Type coercion
* Strict validation

---

### ✅ Section 3 — Field Rules & Constraints

Topics covered:

* `Field()`
* `min_length`
* `max_length`
* `gt`
* `ge`
* `lt`
* `le`
* Pattern validation
* Field descriptions
* Metadata

---

### ✅ Section 4 — Complex & Nested Data

Topics covered:

* List fields
* Dictionary fields
* Set fields
* Tuple fields
* Nested models
* Multi-level nesting
* Lists of nested models
* Enum validation

---

### ✅ Section 5 — Custom Validators

Topics covered:

* Custom validation logic
* `@field_validator`
* `@model_validator`
* Field-level validation
* Model-level validation
* `mode="before"`
* `mode="after"`
* Raising custom validation errors

---

### ✅ Section 6 — In & Out: Serialization

Topics covered:

* Serialization
* Deserialization
* `model_validate()`
* `model_validate_json()`
* `model_dump()`
* `model_dump_json()`
* Including selected fields
* Excluding sensitive fields
* Nested model serialization

---

### ⏳ Section 7 — Model Configuration

Coming soon.

---

### ⏳ Section 8 — Aliases & Computed Fields

Coming soon.

---

### ⏳ Section 9 — Special Data Types

Coming soon.

---

### ⏳ Section 10 — Settings Per Environment

Coming soon.

---

### ⏳ Section 11 — Reading Validation Errors

Coming soon.

---

### ⏳ Section 12 — Real-World Practice

Coming soon.

---

## 📂 Repository Structure

```text
PYDANTIC/
│
├── 01_why_pydantic_exists/
├── 02_building_first_model/
├── 03_field_rules_constraints/
├── 04_complex_nested_data/
├── 05_custom_validators/
├── 06_serialization/
│
└── README.md
```

---

## ⚙️ Installation

Install Pydantic:

```bash
pip install pydantic
```

Check the installed version:

```bash
pip show pydantic
```

---

## 🧪 Basic Example

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


user = User(
    name="Rahul",
    age="25"
)


print(user)
print(type(user.age))
```

Output:

```text
name='Rahul' age=25
<class 'int'>
```

Pydantic validates the input and converts compatible values into the expected types.

---

## 🎯 Learning Goals

The main goals of this repository are:

* Understand Pydantic fundamentals
* Learn runtime data validation
* Build structured data models
* Apply field constraints
* Work with nested data
* Create custom validators
* Understand serialization and deserialization
* Learn model configuration
* Use Pydantic in backend and AI applications
* Build real-world validation projects

---

## 🛠️ Technologies Used

* Python
* Pydantic V2
* JSON
* Python Type Hints
* Git
* GitHub

---

## 🚀 Future Plans

After completing all 12 sections, this repository will include practical projects such as:

* User Registration Validator
* JSON Data Validator
* Configuration Loader
* Inventory Management Models
* CLI Configuration Parser

---

## 📖 Progress

```text
██████████░░░░░░░░░░  6 / 12 Sections Completed
```

**Current Progress: 50%**

---

## ⭐ Purpose

This repository is created for learning, revision, interview preparation, and practical implementation of Pydantic concepts.

The goal is not only to understand the syntax, but also to understand how reliable data validation improves backend systems, APIs, AI applications, and real-world Python projects.

---

## 👨‍💻 Author

**Ankan Haldar**

Python Developer | Backend Development | AI Engineering Learner

---

⭐ If you find this repository useful, consider giving it a star.
