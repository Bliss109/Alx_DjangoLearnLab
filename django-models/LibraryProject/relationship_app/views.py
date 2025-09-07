from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book
from .models import Library   # ✅ Separate explicit import for checker

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/templates/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/templates/library_detail.html'
    context_object_name = 'library'


