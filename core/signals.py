import json
import os
from datetime import datetime
from decimal import Decimal
from io import TextIOWrapper

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.internal_Objects import ImportLine
from core.models import ImportCNAB, Owner, Store, TransactionType, TransactionStore
from projeto import settings


@receiver(post_save, sender=ImportCNAB)
def post_save_Import_CNAB(sender, instance, created=False, **kwargs):
    with transaction.atomic():
        for f in TextIOWrapper(instance.file.file, encoding='utf-8'):
            line = ImportLine(f)
            owner, _ = Owner.objects.get_or_create(
                document=line.document_owner, name=line.name_owner
            )
            store, _ = Store.objects.get_or_create(
                owner=owner, name=line.name_store
            )
            try:
                transaction_type = TransactionType.objects.get(cod=int(line.type))
            except TransactionType.DoesNotExist:
                f = open(settings.BASE_DIR / 'core/json_files/transations.json')
                data = json.load(f)
                data = data.get(str(line.type))
                data.update({'cod': int(line.type)})
                transaction_type = TransactionType.objects.create(**data)
            start_date = datetime.strptime('{} {}'.format(line.date, line.hour), '%Y%m%d %H%M%S')
            TransactionStore.objects.create(
                **{
                    'type':transaction_type,
                    'store': store,
                    'file' :instance,
                    'date': start_date,
                    'value' :Decimal(line.value)/100,
                    'number_card':line.number_card

                }
            )
