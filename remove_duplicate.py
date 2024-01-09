import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemistry.settings')
django.setup()

from django.db.models import Count
from periodic_table.models import Element

# Identify duplicates by atomic number
duplicate_elements = Element.objects.values('atomic_number').annotate(count=Count('atomic_number')).filter(count__gt=1)

# Print the number of duplicates found
print(f"Total duplicate elements: {duplicate_elements.count()}")

# Remove duplicates, keeping one instance
for element in duplicate_elements:
    atomic_number = element['atomic_number']
    elements_to_remove = Element.objects.filter(atomic_number=atomic_number)
    elements_to_keep = elements_to_remove[:1]  # Keep the first instance, slice to keep only one
    elements_to_delete = elements_to_remove.exclude(pk__in=elements_to_keep)
    num_deleted, _ = elements_to_delete.delete()
    print(f"Deleted {num_deleted} duplicates of atomic number {atomic_number}")

# Print the total number of elements after removal
print(f"Total elements after removal: {Element.objects.count()}")
