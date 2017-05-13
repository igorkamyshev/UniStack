from django import template

register = template.Library()


@register.inclusion_tag('app/layout/university_list.html')
def show_university_list(universities):
    return {
        'universities': list(universities),
    }
