# Client Registry

A command-line client registry built with Python as a study project,
focused on practicing data structures, search logic and file persistence.

## Features

- Add clients with name, phone and CPF
- List all registered clients
- Search clients by partial name, case-insensitive
- Remove a client, with confirmation before deleting
- Data persistence with JSON — clients are saved to a file and loaded on startup
- Input validation for empty fields
- Error handling for missing and invalid data files

## Requirements

- Python 3

No external dependencies.

## How to run

```bash
git clone https://github.com/joaohfaria/client-registry.git
cd client-registry
python clientes.py
```

Clients are stored in `clientes.json`, created automatically on first save.

## How it works

Each client is stored as a dictionary:

```python
{
    "nome": "Maria Silva",
    "telefone": "35999998888",
    "cpf": "12345678900"
}
```

All clients are kept in a list, which is written to `clientes.json` after every
operation that changes the data.

Search matches any part of the name and ignores letter case, so searching for
"mar" returns both "Maria" and "Marcos". Removal requires the full name but is
also case-insensitive, and asks for confirmation before deleting.

## Concepts practiced

- Lists and dictionaries
- Loops, conditionals and flow control with `continue` and `break`
- Functions, parameters and return values
- String methods for normalizing user input
- Reading and writing files
- Working with JSON
- Error handling with try/except
- Version control with Git

## Status

Complete as a study project.

## Next steps

- Split the code into separate modules
- Handle clients with duplicate names
- Validate phone and CPF formats