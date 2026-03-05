# CSC230 SQLite Activity

## Folder layout

- `jupyterhub/`: main in-class path
- `local/`: optional local setup path

## In-class default (recommended): JupyterHub

Open:
- `jupyterhub/sqlite_activity_notebook.ipynb`

Flow:
1. Open the notebook in campus [JupyterHub](https://jupyterhub.smith.edu).
2. Run cells top-to-bottom.
3. Complete the activity cells (sanity checks, reset, A -> D).

This notebook uses Python's built-in `sqlite3`, so students do not need MySQL installed.

## Optional local path

### Option A: no conda, no installs

```bash
cd local
python sqlite_test.py
```

### Option B: conda (optional)

```bash
cd local
conda env create -p ./.conda-env -f environment.yml
```

Activate environment:

Mac/Linux:
```bash
conda activate "$(pwd)/.conda-env"
```

Windows (VSCode terminal):

PowerShell:
```powershell
conda activate "$pwd\.conda-env"
```

Command Prompt (`cmd`):
```bat
conda activate "%cd%\.conda-env"
```

Git Bash:
```bash
conda activate "$(pwd)/.conda-env"
```

If activation fails:
```bash
conda info --envs
```
Then activate the full path shown for `.conda-env`.

Run local test:
```bash
python sqlite_test.py
```

Use a custom database file if needed:
```bash
python sqlite_test.py --db my_section.db
```
