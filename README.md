# grafana-backup-s3

Simple tool for backing up & restoring Grafana dashboards and data sources and uploading them to S3 bucket.

Portions based on [ysde/grafana-backup-tool].

## Usage
```
usage: grafana-backup-s3.py [-h] [--restore BACKUP_OBJECT_NAME]

Backups Grafana dashboards and uploads them to S3 bucket. Without any
arguments, backup will be performed.

optional arguments:
  -h, --help            show this help message and exit
  --restore BACKUP_OBJECT_NAME
                        restore backup from given S3 object
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
