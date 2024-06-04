from urllib.parse import urlencode
from django import template
from goods.models import Category


register=template.Library()


@register.simple_tag()
def tag_category():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query) 