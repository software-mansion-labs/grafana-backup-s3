import datetime
import os
import tempfile
import shutil
import json

from gbs3 import grafana
from gbs3.settings import *
from gbs3.util import eprint


def backup(s3):
    timestamp = datetime.datetime.utcnow().isoformat()
    object_name = os.path.join(BACKUP_DIR, timestamp + '.tar.gz')

    with tempfile.TemporaryDirectory() as tmp_dir:
        os.makedirs(os.path.join(tmp_dir, 'data/dashboards'))
        os.makedirs(os.path.join(tmp_dir, 'data/datasources'))

        eprint('fetching dashboards')
        all_dashboards = grafana.all_dashboards()

        eprint('will backup {} dashboards '.format(len(all_dashboards)))

        for dashboard in all_dashboards:
            eprint('*', dashboard['title'])
            data = grafana.get_dashboard(dashboard['uri'])
            save_dashboard(dashboard, data, tmp_dir)

        eprint('fetching datasources')
        datasources = grafana.datasources()

        eprint('will backup {} datasources'.format(len(datasources)))

        for datasource in datasources:
            eprint('*', datasource['name'])
            save_datasource(datasource, tmp_dir)

        eprint('creating backup archive')
        bk = shutil.make_archive(os.path.join(tmp_dir, 'bk'),
                                 format='gztar',
                                 root_dir=os.path.join(tmp_dir, 'data'),
                                 base_dir='./')

        bucket = s3.Bucket(S3_BUCKET_NAME)

        eprint('uploading archive to S3')
        bucket.upload_file(bk, object_name)

        eprint('backup uploaded to:', object_name)


def save_dashboard(dashboard, data, tmp_dir):
    file_name = dashboard['title'] + '.json'
    file_path = os.path.join(tmp_dir, 'data', 'dashboards', file_name)
    with open(file_path, 'w') as f:
        f.write(json.dumps(data))


def save_datasource(datasource, tmp_dir):
    file_name = datasource['name'] + '.json'
    file_path = os.path.join(tmp_dir, 'data', 'datasources', file_name)
    with open(file_path, 'w') as f:
        f.write(json.dumps(datasource))
