# slowly

### hide
- prod.py
- secrets.json

### runserver
- python manage.py runserver --settings=config.settings.base
- python manage.py runserver --settings=config.settings.prod

### Web Crawling
- use postgres
#### Table
- Country
- University

### 정참조
- Product.objects.get(id=1)
- Product.objects.get(id=1).sub_category.name
- Product.objects.get(id=1).sub_category.category.name

### 역참조
- Category.objects.get(id=1)
- Category.objects.get(id=1).category_set.get(id=2)
- Category.objects.get(id=1).category_set.get(id=2).product_set.get(id=1)

**add related_name**
- Category.objects.get(id=1)
- Category.objects.get(id=1).subcategory.get(id=2)
- Category.objects.get(id=1).subcategory.get(id=2).product.get(id=1)

### select_related vs prefetch_related
- [https://docs.djangoproject.com/en/1.11/ref/models/querysets/#select-related](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#select-related)
