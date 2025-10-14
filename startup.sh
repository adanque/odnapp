pip install poetry 
poetry install --no-root 
poetry run gunicorn --bind=0.0.0.0 --workers=2 --timeout=600 load
# poetry run gunicorn --bind=0.0.0.0 --workers=4 --timeout=600 my_app.wsgi:application
# poetry run gunicorn --workers 2 --worker-class uvicorn.workers.UvicornWorker app.main:app --timeout 600