# CSC230 MySQL Python Starter

This folder includes:
- `environment.yml`: conda environment definition
- `requirements.txt`: pip fallback dependencies
- `mysql_test.py`: simple script to verify a MySQL connection
- `mysql_test_notebook.ipynb`: JupyterHub fallback version

## Conda path (recommended)

### 1. Create environment

```bash
conda env create -p ./.conda-env -f environment.yml
```

### 2. Activate environment

```bash
conda activate "$(pwd)/.conda-env"   # Mac/Linux
```

If activation fails, run:

```bash
conda info --envs
```

Then activate the full path shown for `.conda-env`.

### 3. Run connection test

```bash
python mysql_test.py --host 127.0.0.1 --user root --database mysql
```

The script will prompt for a password securely.

### 4. Optional: update environment if file changes

```bash
conda env update -p ./.conda-env -f environment.yml --prune
```

## Backup path (no conda)

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

```bash
source .venv/bin/activate
```

### 3. Install dependency

```bash
pip install -r requirements.txt
```

(Equivalent single-package install: `pip install mysql-connector-python==9.2.0`)

### 4. Run script

```bash
python mysql_test.py --host 127.0.0.1 --user root --database mysql
```

## Escape hatch: JupyterHub notebook

If local setup still fails, use:
- `mysql_test_notebook.ipynb`

Notebook flow:
1. Open the notebook in campus JupyterHub.
2. Edit `HOST`, `PORT`, `USER`, `DATABASE`.
3. Run cells top to bottom and enter password when prompted.
4. If import fails, run `%pip install mysql-connector-python==9.2.0` in a cell, then restart kernel.
