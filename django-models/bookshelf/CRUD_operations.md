
---

## 📄 `CRUD_operations.md`
(collects all of the above in one file)

```markdown
# CRUD Operations on Book Model

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>

## Retrieve
```python
retrieved = Book.objects.get(id=book.id)
retrieved.title, retrieved.author, retrieved.publication_year
# ('1984', 'George Orwell', 1949)

## Update
retrieved.title = "Nineteen Eighty-Four"
retrieved.save()
Book.objects.get(id=book.id).title
# 'Nineteen Eighty-Four'

## Delete
retrieved.delete()
Book.objects.all()
# <QuerySet []>


