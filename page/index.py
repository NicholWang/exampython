from django.core.paginator import Paginator


def get_page(extity,page_num,count = 2):
    books = extity.objects.all()
    p = Paginator(books, count)
    page = p.page(page_num)
    return page.object_list