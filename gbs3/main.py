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
        description='Backups Grafana dashboards and uploads them to S3 bucket.')

    sp = argparser.add_subparsers(dest='command', title='actions')

    sp.add_parser('backup',
                  description='Performs backup.',
                  help='performs backup')

    sp_restore = sp.add_parser('restore',
                               description='Restores latest backup',
                               help='restores latest backup')
    sp_restore.add_argument('object_name', type=str,
                            help='S3 backup object name to restore')

    args = argparser.parse_args()

    eprint('verifying config')

    verify_conf('S3_ACCESS_KEY_ID')
    verify_conf('S3_SECRET_ACCESS_KEY')
    verify_conf('GRAFANA_URL')
    verify_conf('GRAFANA_TOKEN')

    eprint('creating s3 client')

    s3 = boto3.resource('s3',
                        region_name=S3_REGION_NAME,
                        endpoint_url=S3_ENDPOINT_URL,
                        aws_access_key_id=S3_ACCESS_KEY_ID,
                        aws_secret_access_key=S3_SECRET_ACCESS_KEY)

    if args.command == 'backup':
        backup(s3)
    elif args.command == 'restore':
        restore(s3, args.object_name)
