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
- select_related 는 1:1의 관계에서 사용할 수 있고, 혹은 1:N 관계에서 **N**이 사용할 수 있다.
- Product.objects.get(id=1)
- Product.objects.get(id=1).sub_category.name
- Product.objects.get(id=1).sub_category.category.name

### 역참조
- prefetch_related 는 반대로 M:N 에 관계에서 사용할 수 있고, 1:N 의 관계에서 **1**이 사용할 수 있다.
- Category.objects.get(id=1)
- Category.objects.get(id=1).category_set.get(id=2)
- Category.objects.get(id=1).category_set.get(id=2).product_set.get(id=1)

**add related_name**
- Category.objects.get(id=1)
- Category.objects.get(id=1).subcategory.get(id=2)
- Category.objects.get(id=1).subcategory.get(id=2).product.get(id=1)

### select_related vs prefetch_related
- https://docs.djangoproject.com/en/4.0/ref/models/querysets/#select-related
- https://blog.myungseokang.dev/posts/django-query-optimization/
