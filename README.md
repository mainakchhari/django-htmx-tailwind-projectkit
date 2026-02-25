# Django + Htmx + Tailwind (template/starter)

A production-ready Django template designed for Python 3.12, 3.13, and 3.14. Built with modern tooling to ensure a fast developer experience and secure deployments.

> [!NOTE]
> For a simpler version (no htmx/tailwind) see [mainakchhari/django-projectkit](https://github.com/mainakchhari/django-projectkit)

> [!WARNING]
> This template uses the src-layout structure

## Quick Start

Create a new project using the Django CLI. Since this template includes modern configuration files, you must specify them for placeholder replacement using the `-n` (extension) flag:

```bash
django-admin startproject \
  --template=<TEMPLATE_ZIP_URL> \
  -n pyproject.toml,README.md \
  [YOUR_PROJECT_NAME]
```

The `TEMPLATE_ZIP_URL` should be the path to the latest release artifact, unless you want the [latest changes](https://github.com/mainakchhari/django-htmx-tailwind-projectkit/archive/refs/heads/main.zip)

## Next Steps

- copy `.env.dist` to `.env` and get started with `app-admin runserver`
- Uses uv for python tooling. Run `uv sync` to install app and deps
- Run migrations and start local server with `app-admin` (wrapper over [manage.py](src/manage.py))
- Run `tailwindcss -i static/pre/input.css -o static/css/main.css --watch` during dev to auto-preprocess css changes to output; run with --minify instead of --watch in production
- Ships with some opinionated deps - environ, htmx, tailwind
- whitenoise serves assets in production (needs collectstatic)

## Tooling Choices

This is an opinionated template focused on ease of use and good practices:

- [uv](https://astral.sh/uv): Handles dependency management and virtual environments with extreme speed. Run `uv sync` to generate your `uv.lock`.
- [django-environ](https://github.com/joke2k/django-environ): Manages configuration via environment variables, keeping secrets secure.
- [whitenoise](https://whitenoise.readthedocs.io/): Efficiently serves static files directly from Django, simplifying Docker and production deployments.
- [django-rich](https://github.com/adamchainz/django-rich): Adds rich color output to test runners, runserver
- [django-htmx](https://github.com/adamchainz/django-htmx?tab=readme-ov-file): template tags, middlware, etc
- [pytailwindcss](https://pypi.org/project/pytailwindcss/)

## Production

- run app-admin check --deploy before you running in production
- versioning is maintained through `src/{{ project_name }}/__about__.py` -- single point of configuration

## todo

- tests (see django/django)
