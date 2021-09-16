from django.db import models

def create_path_import_file(instance, filename):
    directory = 'file/id_store/{}/import/'.format(instance.store.id)
    full_path = str(directory) + "/%s" % (filename)
    return full_path

OperationChocie = (
    ('ENTRADA', '+'),
    ('SAIDA', '-'),
)

class TimestampableMixin(models.Model):
    data_cadastro = models.DateTimeField(auto_now_add=True)
    date_modificado = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Store(TimestampableMixin):
    name = models.CharField(max_length=120)
    document = models.CharField(max_length=14)

class TransactionType(models.Model):
    cod = models.IntegerField()
    description = models.CharField(max_length=255)
    operation = models.CharField(max_length=10, choices=OperationChocie)

class TransactionStore(TimestampableMixin):
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    documentRecipient = models.CharField(max_length=18)
    numberCard = models.IntegerField()

class importCNAD(TimestampableMixin):
    file = models.FileField(upload_to=create_path_import_file)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
