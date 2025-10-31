product_index = 2
products_indexes = [10, 11]

search_words = ['desk', 'corner', 'table', 'screen']
products_test_data = [(0, 5, 235.00), (2, 5, 602.50)]

sort_indexes = [2, 3, 4]

sort_verifications = {
    'Name (A-Z)': 'assert_sorted_by_name_asc',
    'Price - Low to High': 'assert_sorted_by_price_asc',
    'Price - High to Low': 'assert_sorted_by_price_desc',
}
