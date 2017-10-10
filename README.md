# grafana-backup-s3

Simple tool for backing up & restoring Grafana dashboards and data sources and uploading them to S3 bucket. It also works with DigitalOcean Spaces.

Portions based on [ysde/grafana-backup-tool].

## Usage
```
$ ./grafana-backup-s3.py -h
usage: grafana-backup-s3.py [-h] {backup,restore} ...

Backups Grafana dashboards and uploads them to S3 bucket.

optional arguments:
  -h, --help        show this help message and exit

actions:
  {backup,restore}
    backup          performs backup
    restore         restores latest backup

$ ./grafana-backup-s3.py backup -h
usage: grafana-backup-s3.py backup [-h]

Performs backup.

optional arguments:
  -h, --help  show this help message and exit

$ ./grafana-backup-s3.py restore -h
usage: grafana-backup-s3.py restore [-h] object_name

Restores latest backup

positional arguments:
  object_name  S3 backup object name to restore

optional arguments:
  -h, --help   show this help message and exit
```

## Configuration

This tool is configurable via environment variables or `.env` file:

Variable | Required | Description
---------|:--------:|------------
`S3_ACCESS_KEY_ID` | yes | S3 access key.
`S3_SECRET_ACCESS_KEY` | yes | S3 secret key.
`S3_REGION_NAME` | no | S3 region name.
`S3_ENDPOINT_URL` | no | S3 endpoint url (useful for DigitalOcean Spaces).
`S3_BUCKET_NAME` | no | S3 bucket name for backup objects.
`GRAFANA_URL` | yes | Base URL for Grafana instance.
`GRAFANA_TOKEN` | yes | Grafana API token, requires Admin privileges.
`BACKUP_DIR` | no | Name prefix for backup objects. Default value: `grafana-backups/`.

## Dependencies

Requires `dotenv`, `boto3` and `requests`, see [requirements.txt](requirements.txt).

## License

See the [LICENSE] file for license rights and limitations (MIT).

[LICENSE]: https://github.com/SoftwareMansion/grafana-backup-s3/blob/master/LICENSE.txt

[ysde/grafana-backup-tool]: https://github.com/ysde/grafana-backup-tool
