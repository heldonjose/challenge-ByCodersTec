from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from core.models import ImportCNAB, TransactionType, TransactionStore


@admin.register(ImportCNAB)
class ImportCNABAdmin(admin.ModelAdmin):
    list_display = ('file',)


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass
    list_display = ('cod', 'description', 'operation',)


@admin.register(TransactionStore)
class TransactionStoreAdmin(admin.ModelAdmin):
    list_display = ('get_type', 'get_store', 'date', 'value', 'number_card')

    def get_store(self, obj):
        return obj.store.name
    get_store.short_description = 'Store'
    get_store.admin_order_field = 'store__name'

    def get_type(self, obj):
        return obj.type.description
    get_type.short_description = 'Type'
    get_type.admin_order_field = 'type__description'
