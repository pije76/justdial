# -*- coding: utf-8 -*-
import os
import datetime
# import calendar
import json
import logging
import decimal

from decimal import Decimal

# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template.loader import render_to_string
import csv

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Import Students"

    def add_arguments(self, parser):
        parser.add_argument('--path',  action='store', dest='csv_path', required=True,
                            type=str, help='Csv file path')
        parser.add_argument(
            '--commit',
            action='store_true',
            dest='commit',
            default=False,
            help='Commit the transaction')

    @transaction.atomic
    def handle(self, *args, **options):
        sid = transaction.savepoint()
        try:
            csv_file = options['csv_path']

            with open(csv_file, 'rt') as f:
                readCSV = csv.reader(csv_file, delimiter=',')
                for row in readCSV:
                    print(row)
                    print(row[0])
                    print(row[0], row[1], row[2],)

            eid = transaction.savepoint()
        except Exception as ex:
            logger.error("{}".format(ex))
            logger.info("Error occurred, transaction rollback.")
            transaction.savepoint_rollback(sid)
            raise
        else:
            if options['commit']:
                logger.info("Successful commit")
                transaction.savepoint_commit(eid)
            else:
                logger.info("Successful dry-run")
                transaction.savepoint_rollback(sid)
