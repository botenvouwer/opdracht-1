import csv

from constants import FILE_PATH

cinecenter_bar_verkoop_csv = FILE_PATH / "Cinecenter-product-sales.csv"

data_list = []

with open(cinecenter_bar_verkoop_csv, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Append the row dictionary to the data list
        data_list.append({
            'order_id': row['order_id'],
            'product_id': row['product_id'],
            'product_name': row['product_name'],
            'category': row['category'],
            'price': float(row['price']),
            'worth': float(row['worth']),
            'status': row['status'],
            'created_at': row['created_at']
        })

# Now, data_list contains a list of dictionaries representing each row in the CSV file
for data in data_list[0:3]:
    print(data)


