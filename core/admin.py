from django.contrib import admin
from oscar.core.loading import get_model

# Register your models here.
Source = get_model('core', 'Source')
Status = get_model('core', 'Status')
Client = get_model('core', 'Client')
Manager = get_model('core', 'Manager')
Document = get_model('core', 'Document')
TownHouse = get_model('core', 'TownHouse')
Construction = get_model('core', 'Construction')
Locality = get_model('core', 'Locality')
ConstructionStage = get_model('core', 'ConstructionStage')
Card = get_model('core', 'Card')

admin.site.register(Source)
admin.site.register(Status)
admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Document)
admin.site.register(TownHouse)
admin.site.register(Construction)
admin.site.register(Locality)
admin.site.register(ConstructionStage)
admin.site.register(Card)
