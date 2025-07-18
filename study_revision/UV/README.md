Here's a complete `README.md` tutorial to help you get started with the **[uv](https://github.com/astral-sh/uv)** Python package manager, which is a **fast, drop-in replacement** for `pip` and `virtualenv`, developed by [Astral](https://astral.sh).

---

# 🚀 UV - Fast Python Package Manager

**`uv`** is an ultra-fast Python package manager and virtual environment manager, written in Rust, intended to be a drop-in replacement for `pip` and `virtualenv`. It supports most common Python workflows, dramatically improves performance, and includes resolver improvements.

---

## ✨ Features

* 🔥 Super fast dependency resolution & installation
* 📦 Drop-in replacement for `pip`, `pip-tools`, and `virtualenv`
* 🌍 Works across platforms (Linux, macOS, Windows)
* 📁 Deterministic lock files (`uv pip compile`)
* 💡 Works with `pyproject.toml`

---

## 📦 Installation

You can install `uv` using `pipx` or by downloading the binary directly:

### Option 1: Install via pipx (Recommended)

```bash
pipx install uv
```

### Option 2: Install via Homebrew (macOS)

```bash
brew install astral-sh/astral/uv
```

### Option 3: Install via pre-built binary

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

After installation, ensure `uv` is in your `PATH`.

---

## 🔰 Basic Usage

### ✅ Create a virtual environment

```bash
uv venv
```

### 📍 Activate virtual environment

**Linux/macOS**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```bash
.venv\Scripts\Activate.ps1
```

---

## 🧪 Installing Dependencies

### 📌 Install from `requirements.txt`

```bash
uv pip install -r requirements.txt
```

### 📌 Install packages

```bash
uv pip install requests pandas
```

### 🔒 Compile deterministic lock files (like pip-tools)

```bash
uv pip compile pyproject.toml --output requirements.txt
```

---

## 🧹 Removing/Uninstalling Packages

```bash
uv pip uninstall requests
```

---

## 🔄 Updating Packages

```bash
uv pip install --upgrade requests
```

---

## 📂 Managing pyproject.toml Projects

You can use `uv` directly with `pyproject.toml`:

```bash
uv pip install
```

This will install dependencies from `[project.dependencies]`.

---

## 🔍 Search for Packages

```bash
uv pip search <package-name>
```

---

## 📚 Helpful Commands

| Command                              | Description                         |
| ------------------------------------ | ----------------------------------- |
| `uv venv`                            | Create a virtual environment        |
| `uv pip install <pkg>`               | Install a package                   |
| `uv pip install -r requirements.txt` | Install from requirements file      |
| `uv pip uninstall <pkg>`             | Uninstall a package                 |
| `uv pip compile`                     | Compile lock files (like pip-tools) |
| `uv pip freeze`                      | Show installed packages             |
| `uv pip list`                        | List installed packages             |
| `uv pip search`                      | Search for packages on PyPI         |

---

## 💡 Example Workflow

```bash
# Step 1: Create and activate environment
uv venv
source .venv/bin/activate

# Step 2: Install dependencies
uv pip install fastapi uvicorn

# Step 3: Freeze to requirements
uv pip freeze > requirements.txt

# Step 4: Run your app
uvicorn main:app --reload
```

---

## 🧪 Testing & Speed Comparison

You can compare `uv` with `pip`:

```bash
time pip install -r requirements.txt  # Traditional
time uv pip install -r requirements.txt  # UV (much faster)
```

---

## 🛠️ Troubleshooting

* Ensure `uv` is in your `PATH`
* Use `--help` with any command to explore options:

  ```bash
  uv pip --help
  ```

---

## 📎 Links

* [GitHub Repo](https://github.com/astral-sh/uv)
* [Official Docs](https://astral.sh/docs/uv/)
* [PyPI Package](https://pypi.org/project/uv/)

---

## 🧑‍💻 Maintainers

Brought to you by [Astral](https://astral.sh), creators of Ruff and other blazing fast Python tools.

---


To **uninstall all packages** in a Python environment using `uv`, you can do the following:

---

## 🔥 Uninstall All Packages Using `uv pip freeze`

```bash
uv pip freeze | xargs uv pip uninstall -y
```

### ✅ What this does:

1. `uv pip freeze` – lists all installed packages.
2. `xargs uv pip uninstall -y` – pipes each one into an uninstall command with `-y` to confirm automatically.

---

## 🧼 Alternative: Delete the Virtual Environment

If you're using a virtual environment created via `uv venv`, the cleanest way is just to delete the `.venv` folder:

```bash
rm -rf .venv
uv venv  # (optional) recreate it fresh
```

---
