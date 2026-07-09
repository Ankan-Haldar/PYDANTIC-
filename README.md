# 🛡️ PYDANTIC — Learning Notes & Practice

A structured collection of **Pydantic V2 notes, concepts, and practical code examples**.

This repository documents my step-by-step journey of learning Pydantic, from basic data validation to nested models, custom validators, serialization, model configuration, aliases, special data types, environment settings, error handling, and real-world applications.

---

## 📌 About Pydantic

Pydantic is a Python library for **data validation and parsing using Python type hints**.

It helps developers:

* Validate incoming data
* Convert compatible data types
* Create structured data models
* Apply field-level constraints
* Validate nested and complex data
* Write custom validation logic
* Serialize models into dictionaries and JSON
* Manage application configuration
* Validate special data types
* Generate clear validation errors

Pydantic is widely used in:

* FastAPI applications
* Backend development
* AI and LLM applications
* Data pipelines
* Configuration management
* API request and response validation
* Automation scripts
* Structured AI output validation

---

# 📚 Learning Roadmap

This repository is divided into **12 sections**.

---

## ✅ Section 1 — Why Pydantic Exists

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

## ✅ Section 2 — Building Your First Model

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

## ✅ Section 3 — Field Rules & Constraints

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

## ✅ Section 4 — Complex & Nested Data

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

## ✅ Section 5 — Custom Validators

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

## ✅ Section 6 — In & Out: Serialization

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

## ✅ Section 7 — Model Configuration

Topics covered:

* `ConfigDict`
* `model_config`
* Extra field handling
* `extra="forbid"`
* `extra="ignore"`
* `extra="allow"`
* Frozen models
* Assignment validation
* String whitespace removal
* Lowercase conversion
* Uppercase conversion

---

## ✅ Section 8 — Aliases & Computed Fields

Topics covered:

* Field aliases
* `alias`
* `validation_alias`
* `serialization_alias`
* `by_alias=True`
* Computed fields
* `@computed_field`
* Calculated model properties
* Alias-based serialization

---

## ✅ Section 9 — Special Data Types

Topics covered:

* `EmailStr`
* `HttpUrl`
* UUID validation
* Date validation
* Time validation
* Datetime validation
* `timedelta`
* IP address validation
* `SecretStr`
* Secret value handling

---

## ✅ Section 10 — Settings Per Environment

Topics covered:

* `pydantic-settings`
* `BaseSettings`
* Environment variables
* `.env` files
* `SettingsConfigDict`
* Database configuration
* API key configuration
* Default settings values
* Development configuration
* Production configuration
* `.env.example`
* Secret management basics

---

## ⏳ Section 11 — Reading Validation Errors

Coming soon.

Planned topics:

* `ValidationError`
* `errors()`
* `error_count()`
* `json()`
* Error locations
* Error messages
* Error types
* Nested validation errors
* API-friendly error formatting

---

## ⏳ Section 12 — Real-World Practice

Coming soon.

Planned projects:

* User Registration Validator
* Inventory Management Models
* CLI Configuration Parser

---

# 📂 Repository Structure

```text
PYDANTIC/
│
├── Section 1/
│   └── Why Pydantic Exists examples
│
├── Section 2/
│   └── First Model examples
│
├── Section 3/
│   └── Field Rules & Constraints examples
│
├── Section 4/
│   └── Complex & Nested Data examples
│
├── Section 5/
│   └── Custom Validator examples
│
├── Section 6/
│   └── Serialization examples
│
├── Section 7/
│   └── Model Configuration examples
│
├── Section 8/
│   └── Alias & Computed Field examples
│
├── Section 9/
│   └── Special Data Type examples
│
├── Section 10/
│   └── Settings examples
│
└── README.md
```

---

# ⚙️ Installation

Install Pydantic:

```bash
pip install pydantic
```

For email validation:

```bash
pip install email-validator
```

For application settings:

```bash
pip install pydantic-settings
```

Or install everything together:

```bash
pip install pydantic email-validator pydantic-settings
```

Check the installed Pydantic version:

```bash
pip show pydantic
```

---

# 🧪 Basic Example

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

# 🎯 Learning Goals

The main goals of this repository are:

* Understand Pydantic fundamentals
* Learn runtime data validation
* Build structured data models
* Apply field constraints
* Work with nested data
* Create custom validators
* Understand serialization and deserialization
* Configure model behavior
* Work with aliases
* Create computed fields
* Validate real-world data types
* Manage environment-based configuration
* Understand validation errors
* Build practical Pydantic projects

---

# 🛠️ Technologies Used

* Python
* Pydantic V2
* Pydantic Settings
* Python Type Hints
* JSON
* Environment Variables
* Git
* GitHub

---

# 🚀 Future Plans

After completing all 12 sections, this repository will include practical projects such as:

### 👤 User Registration Validator

A complete user registration validation system covering:

* Username validation
* Email validation
* Password rules
* Password confirmation
* Age validation
* Optional profile information

### 📦 Inventory Management Models

A structured inventory validation system covering:

* Product models
* Price validation
* Quantity validation
* Product categories
* Nested supplier information
* Computed inventory values

### ⚙️ CLI Configuration Parser

A configuration management project covering:

* Environment variables
* `.env` files
* Default configuration
* Type conversion
* Secret values
* Development and production settings

---

# 📖 Progress

```text
█████████████████░░░  10 / 12 Sections Completed
```

**Current Progress: 83%**

| Section | Topic                     | Status      |
| ------- | ------------------------- | ----------- |
| 01      | Why Pydantic Exists       | ✅ Completed |
| 02      | Building Your First Model | ✅ Completed |
| 03      | Field Rules & Constraints | ✅ Completed |
| 04      | Complex & Nested Data     | ✅ Completed |
| 05      | Custom Validators         | ✅ Completed |
| 06      | Serialization             | ✅ Completed |
| 07      | Model Configuration       | ✅ Completed |
| 08      | Aliases & Computed Fields | ✅ Completed |
| 09      | Special Data Types        | ✅ Completed |
| 10      | Settings Per Environment  | ✅ Completed |
| 11      | Reading Validation Errors | ⏳ Pending   |
| 12      | Real-World Practice       | ⏳ Pending   |

---

# ⭐ Purpose

This repository is created for:

* Learning
* Revision
* Interview preparation
* Backend development practice
* API development preparation
* AI Engineering preparation
* Real-world Python data validation practice

The goal is not only to learn Pydantic syntax, but also to understand how reliable data validation improves backend systems, APIs, AI applications, and production Python projects.

---

# 👨‍💻 Author

**Ankan Haldar**

Python Developer | Backend Development | AI Engineering Learner

---

⭐ If you find this repository useful, consider giving it a star.
