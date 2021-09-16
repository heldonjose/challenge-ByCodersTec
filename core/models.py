from django.db import models


def create_path_import_file(instance, filename):
    directory = 'file/import/'
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


class Owner(TimestampableMixin):
    document = models.CharField(max_length=18, null=True, unique=True)
    name = models.CharField(max_length=120)


class Store(TimestampableMixin):
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=120)


class TransactionType(models.Model):
    cod = models.IntegerField(unique=True)
    description = models.CharField(max_length=255)
    operation = models.CharField(max_length=10, choices=OperationChocie)


class ImportCNAB(TimestampableMixin):
    file = models.FileField(upload_to=create_path_import_file)


class TransactionStore(TimestampableMixin):
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    file = models.ForeignKey(ImportCNAB, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    number_card = models.CharField(max_length=20, null=True)
