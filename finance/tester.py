


person = [{'id': 3, 'username': 'nic', 'hash': '$6$rounds=656000$fMFN1Uipdi6w64Ks$b5qQgOXwaCQ050hvnEJ6vZ2dxuoqy5S0TWU9420mR6DLH9UEIdsa6j2T7y3nmeIHLXc8UMsjXhBTFQKSCRxID.', 'cash': 2203.0799999999995}]

data = [{'transaction_number': 1, 'stock_name': 'GOOGL', 'timestamp': '2018-01-08 16:00:00', 'price': 1114.21, 'shares': 2, 'user_id': 3}, {'transaction_number': 2, 'stock_name': 'GOOGL', 'timestamp': '2018-01-09', 'price': 1114.21, 'shares': 2, 'user_id': 3}, {'transaction_number': 3, 'stock_name': 'GOOGL', 'timestamp': '2018-01-09', 'price': 1114.21, 'shares': 1, 'user_id': 3}, {'transaction_number': 4, 'stock_name': 'BTC', 'timestamp': '2018-01-09', 'price': 0.23, 'shares': 5, 'user_id': 3}, {'transaction_number': 5, 'stock_name': 'BTC', 'timestamp': '2018-01-09', 'price': 0.23, 'shares': 8, 'user_id': 3}, {'transaction_number': 6, 'stock_name': 'BTC', 'timestamp': '2018-01-09 01:47:37.068619', 'price': 0.23, 'shares': 10, 'user_id': 3}]

SELECT foo, count(bar) AS tot_bar_count FROM mytable GROUP BY bar ORDER BY tot_bar_count DESC