from .base import ShopifyDatedResourceModel
from ..encoders import ShopifyDjangoJSONEncoder
from django.db import models
from jsonfield import JSONField
import shopify


class Webhook(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Webhook

    topic = models.CharField(max_length = 64)
    address = models.URLField()
    format = models.CharField(max_length = 4)
    fields = JSONField(null = True, dump_kwargs = {'cls': ShopifyDjangoJSONEncoder})
    metafield_namespaces = JSONField(null = True)
