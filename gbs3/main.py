import argparse

import boto3

from gbs3.backup import backup
from gbs3.restore import restore
import gbs3.settings
from gbs3.settings import *
from gbs3.util import eprint


def verify_conf(conf_name):
    if not getattr(gbs3.settings, conf_name):
        eprint('missing config option {}'.format(conf_name))
        exit(1)


def main():
    argparser = argparse.ArgumentParser(
        description='Backups Grafana dashboards and uploads them to S3 bucket. '
                    'Without any arguments, backup will be performed.')
    argparser.add_argument('--restore', type=str, metavar='BACKUP_OBJECT_NAME',
                           help='restore backup from given S3 object')
    args = argparser.parse_args()

    eprint('veryfing config')

    verify_conf('S3_ACCESS_KEY_ID')
    verify_conf('S3_SECRET_ACCESS_KEY')
    verify_conf('GRAFANA_URL')
    verify_conf('GRAFANA_TOKEN')

    eprint('creating s3 client')

    s3 = boto3.client('s3',
                      region_name=S3_REGION_NAME,
                      endpoint_url=S3_ENDPOINT_URL,
                      aws_access_key_id=S3_ACCESS_KEY_ID,
                      aws_secret_access_key=S3_SECRET_ACCESS_KEY)

    if args.restore:
        restore(s3, args.restore)
    else:
        backup(s3)
