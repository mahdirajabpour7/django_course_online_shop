from django import template

register = template.Library()


@register.filter
def only_comment_comment(comments):
    return comments.filter(active = True )
