import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

__all__ = [
    'S3_ACCESS_KEY_ID',
    'S3_SECRET_ACCESS_KEY',
    'S3_REGION_NAME',
    'S3_ENDPOINT_URL',
    'S3_BUCKET_NAME',
    'GRAFANA_URL',
    'GRAFANA_TOKEN',
    'BACKUP_DIR'
]

S3_ACCESS_KEY_ID = os.environ.get('S3_ACCESS_KEY_ID')
S3_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET_ACCESS_KEY')
S3_REGION_NAME = os.environ.get('S3_REGION_NAME')
S3_ENDPOINT_URL = os.environ.get('S3_ENDPOINT_URL')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
GRAFANA_URL = os.environ.get('GRAFANA_URL')
GRAFANA_TOKEN = os.environ.get('GRAFANA_TOKEN')
BACKUP_DIR = os.environ.get('BACKUP_DIR', 'grafana-backups/')

if GRAFANA_URL is not None and GRAFANA_URL[-1] == '/':
    GRAFANA_URL = GRAFANA_URL[:-1]
