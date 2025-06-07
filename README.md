# CIVIS - AI Policy Document Compliance Audit Checker Backend Application

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
## If pip install does not work make sure you install it manually and uv --version should works
pip install uv
make venv
source .venv/bin/activate
export SOURCE_DIR=$(pwd)/src
```

## Usage

## Setup Project

### Create virtual env using `uv`

```
$ make venv
```

### Run and fix lint errors

```
$ make fix
```

### Install dependences

```
$ make install
```


## Initialize Database migration using Alembic

### Step 1: Initialize alembic inside source directory
```
$ alembic init -t async src/civis_backend_policy_analyser/alembic
```

### Step 2: Create data base tables revisions for the SQLAlechemy models to generate database tables.
```
$ alembic revision --autogenerate -m "<Revision-Message>"
```

### Step 3: Create Database migration or execute Database queries using alembic.
```
$ alembic upgrade head
```

## Run Fast API Application localhost server.

```
export PYTHONPATH=$(pwd)/src:$PYTHONPATH
make run
```

## Test

```
export PYTHONPATH=$(pwd)/src:$PYTHONPATH
make test
make cov
```

## Postgress Commands

### Connect to your database.
```
psql -U <username> -d <database_name>
```
### Command list tables in the current schema.
```
\dt
```
 ### Command shows table schema
 ```
 \d+ <table_name>
 ```