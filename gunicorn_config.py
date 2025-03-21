import os
import multiprocessing

size = int(os.getenv("SIZE", 1))
# Maximum 5 worker per 128MB
workers = min(multiprocessing.cpu_count() * 2 + 1, size * 1)
timeout = int(os.getenv("GUNICORN_TIMEOUT", 120))
