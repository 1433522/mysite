from django import template
from django.db.models import Count
from ..models import Article,Category

register = template.Library()

@register.filter(name='weekchinese')
def weekchinese(englishweek):
    englishweek_list = list(englishweek)
    if englishweek_list[-1] == '0':
        englishweek_list[-1] = '日'
    elif englishweek_list[-1] == '1':
        englishweek_list[-1] = '一'
    elif englishweek_list[-1] == '2':
        englishweek_list[-1] = '二'
    elif englishweek_list[-1] == '3':
        englishweek_list[-1] = '三'
    elif englishweek_list[-1] == '4':
        englishweek_list[-1] = '四'
    elif englishweek_list[-1] == '5':
        englishweek_list[-1] = '五'
    else:
        englishweek_list[-1] = '六'
    chineseweek = ''.join(englishweek_list)
    return chineseweek 

from django.utils.html import format_html
@register.simple_tag
def list_page(curr_page,loop_page):
    offset = abs(curr_page - loop_page)
    if offset < 3:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        else:
            page_ele = '<li><a href="?page=%s">%s</a></li>'%(loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ''

from django.utils.html import format_html
@register.simple_tag
def search_page(query,curr_page,loop_page):
    offset = abs(curr_page - loop_page)
    if offset < 3:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href="?search=%s&page=%s">%s</a></li>'%(query,loop_page,loop_page)
        else:
            page_ele = '<li><a href="?search=%s&page=%s">%s</a></li>'%(query,loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ''

