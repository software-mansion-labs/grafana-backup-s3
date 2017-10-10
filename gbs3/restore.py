import json
import tempfile
import tarfile

from gbs3 import grafana
from gbs3.settings import *
from gbs3.util import eprint


def restore(s3, object_name):
    bucket = s3.Bucket(S3_BUCKET_NAME)
    with tempfile.TemporaryFile() as f:
        eprint('downloading', object_name)
        bucket.download_fileobj(object_name, f)

        f.seek(0)

        eprint('opening archive')
        with tarfile.open(fileobj=f, mode='r') as tar:
            dbs = list(dashboards(tar))
            dss = list(datasources(tar))
            eprint('found {0} dashboards and {1} datasources'
                   .format(len(dbs), len(dss)))

            eprint('restoring dashboards')
            for tarinfo in dbs:
                db = json.load(tar.extractfile(tarinfo))
                eprint('*', db['dashboard']['title'])
                del db['dashboard']['id']
                db = {'dashboard': db['dashboard']}
                grafana.create_or_update_dashboard(json.dumps(db))

            eprint('restoring datasources')
            for tarinfo in dss:
                ds = json.load(tar.extractfile(tarinfo))
                eprint('*', ds['name'])
                grafana.create_datasource(json.dumps(ds))


def dashboards(tar):
    for tarinfo in tar:
        if tarinfo.isreg() and tarinfo.name.startswith('./dashboards'):
            yield tarinfo


def datasources(tar):
    for tarinfo in tar:
        if tarinfo.isreg() and tarinfo.name.startswith('./datasources'):
            yield tarinfo
