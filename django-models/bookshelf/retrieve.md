
---

## 📄 `retrieve.md`
```markdown
# Retrieve Operation

```python
from bookshelf.models import Book
retrieved = Book.objects.get(id=book.id)
retrieved.title, retrieved.author, retrieved.publication_year
# ('1984', 'George Orwell', 1949)

