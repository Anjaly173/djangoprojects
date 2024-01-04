
from shop.models import Category
def menu_links(request):
    a=Category.objects.all()
    return {'links':a}