from django.contrib import admin
from cashmachine.models import Card, LogRecord


class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'balance', 'blocked', 'pin_attempts_made']
    readonly_fields = ['id', 'pin']


class LogRecordAdmin(admin.ModelAdmin):
    list_display = ['card', 'operation', 'created_at', 'amount',
                    'balance_after_operation']
    readonly_fields = list_display

    list_filter = ('operation',)


admin.site.register(Card, CardAdmin)
admin.site.register(LogRecord, LogRecordAdmin)
