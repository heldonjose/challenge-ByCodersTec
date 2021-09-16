from decimal import Decimal

from django.db import models
from django.db.models import Sum


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


class Company(TimestampableMixin):
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=120)

    @property
    def total_imports(self):
        return self.transactions.all().values_list('file__id', flat=True).distinct().count()

    @property
    def total_in(self):
        return self.transactions.filter(type__operation='ENTRADA').count()

    @property
    def total_out(self):
        return self.transactions.filter(type__operation='SAIDA').count()

    @property
    def total_balance(self):
        sum = self.transactions.filter(type__operation='ENTRADA').aggregate(Sum('value'))
        sub = self.transactions.filter(type__operation='SAIDA').aggregate(Sum('value'))
        sum = sum.get('value__sum') if sum.get('value__sum') else 0
        sub =  sub.get('value__sum') if  sub.get('value__sum') else 0
        total = sum - sub
        return Decimal(sum - sub)


class TransactionType(models.Model):
    cod = models.IntegerField(unique=True)
    description = models.CharField(max_length=255)
    operation = models.CharField(max_length=10, choices=OperationChocie)


class ImportCNAB(TimestampableMixin):
    file = models.FileField(upload_to=create_path_import_file)


class TransactionStore(TimestampableMixin):
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    store = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='transactions')
    file = models.ForeignKey(ImportCNAB, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=15, decimal_places=2)
    number_card = models.CharField(max_length=20, null=True)
