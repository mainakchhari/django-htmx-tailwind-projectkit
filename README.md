# Django + Htmx + Tailwind (template/starter)

## Instructions

- copy `.env.dist` to `.env` and get started with `app-admin runserver`
- Uses uv for python tooling. Run `uv sync` to install app and deps
- Can use gunicorn (production) or start script (app-admin) with runserver to run the server (primary entrypoint). 
- Run `tailwindcss -i static/pre/input.css -o static/css/main.css --watch` during dev to auto-preprocess css changes to output; run with --minify instead of --watch in production
- Ships with some opinionated deps - environ, htmx, tailwind
- whitenoise serves assets in production (needs collectstatic)

## Production

- run app-admin check --deploy before you running in production
- versioning is maintained through `src/config/__about__.py` -- single point of configuration

## todo

- tests (see django/django)
- CI/CD (integrate starterkit into existing repo)
