from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from core.models import ImportCNAB, TransactionType, TransactionStore, Owner, Company


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('document', 'name')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('get_owner', 'name')

    def get_owner(self, obj):
        return obj.owner.name

    get_owner.short_description = 'Owner'
    get_owner.admin_order_field = 'owner__name'

@admin.register(ImportCNAB)
class ImportCNABAdmin(admin.ModelAdmin):
    list_display = ('file',)


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass
    list_display = ('cod', 'description', 'operation',)


@admin.register(TransactionStore)
class TransactionStoreAdmin(admin.ModelAdmin):
    list_filter = ('store', 'type__operation')
    list_display = ('get_type', 'get_operation', 'get_store', 'date', 'value', 'number_card')

    def get_store(self, obj):
        return obj.store.name

    get_store.short_description = 'Store'
    get_store.admin_order_field = 'store__name'

    def get_operation(self, obj):
        return obj.type.operation

    get_operation.short_description = 'Operation'
    get_operation.admin_order_field = 'type__operation'

    def get_type(self, obj):
        return obj.type.description

    get_type.short_description = 'Type'
    get_type.admin_order_field = 'type__description'
