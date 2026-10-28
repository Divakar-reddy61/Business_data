# Business Employment Data

A Django project for loading New Zealand business employment data from the
September 2022 quarter CSV file into a SQLite database.

## Requirements

- Python 3.10 or later
- Django 5.2

## Setup

From the project root, create and activate a virtual environment, then install
Django:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "Django>=5.2,<5.3"
```

Apply database migrations and start the development server:

```powershell
python manage.py migrate
python manage.py runserver
```

The project is then available at <http://127.0.0.1:8000/>.

## Data endpoints

- `GET /insert_data/` reads the CSV and inserts its rows into the `Business`
  table.
- `GET /delete_data/` deletes every row in the `Business` table.
- `/admin/` opens the Django admin site. Create an administrator with
  `python manage.py createsuperuser`.

**Warning:** These data endpoints do not require authentication. The delete
endpoint removes all imported records; do not expose this development project
to an untrusted network.

The CSV file, `Business-employment-data-september-2022-quarter-csv.csv`, is
included in the project root. The current import view uses a hard-coded
Windows file path, so update that path in `app/views.py` if the project is
located elsewhere before using `/insert_data/`.
