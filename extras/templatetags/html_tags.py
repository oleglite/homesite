from django import template

register = template.Library()


@register.simple_tag
def link_or_text(name='', href='', html_attrs='', append=''):
    if href:
        if not name:
            name = href
        link = '<a href="%s" html_attrs>%s</a>' % (href, name)
    elif html_attrs:
        link = '<span html_attrs>%s</span>' % name
    else:
        link = ''
    return link + append

@register.simple_tag
def email(address):
    return '<a href="mailto:{0}">{0}</a>'.format(address)