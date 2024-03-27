'''
5. Advanced Tuple Techniques: Joining and Nesting in Python
Task 1: Product Catalog Merging
Utilize tuple joining to combine multiple product catalogs.

Problem Statement:
You are managing the product catalogs for an online store. Each catalog is a tuple of products, and each product is a tuple containing the product name and price. Merge multiple catalogs into a single tuple.

Write a function to join two or more product catalogs into one.
Display the combined catalog, ensuring that it maintains the order of products as they were in their original catalogs.
'''

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def merge_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog

merged_catalog = merge_catalogs(catalog1, catalog2)
print("Combined Catalog:")
for product in merged_catalog:
    print(product)
