from django import template

register = template.Library()


@register.filter
def translate_number(number):
    number=str(number)
    tt=number.maketrans("0123456789" , "۰١٢٣٤٥٦٧٨٩")
    translated_num = number.translate(tt)
    return translated_num





