#! python3

redis = {'host': '127.0.0.1',
         'port': 6379,
         'database': 0,     # 德州是10，捕鱼是0
         'password': None}

db = {'host': '127.0.0.1',
      'port': 3306,
      'user': 'fishapp',
      'passwd': '123ab?Cbaddd',
      'database': 'fish_db'}

logdb = {'host': '127.0.0.1',
         'port': 3306,
         'user': 'fishapp',
         'passwd': '123ab?Cbaddd',
         'database': 'fish_logdb'}

#需要根据实际情况配置本地log路径
applog={'path_server': '/Users/yangyue/fish_server',
        'path_tool': '/Users/yangyue/fish_test_tool',
        'host': '127.0.0.1'}

web_host = "127.0.0.1:9100"
web_domain = "sqfish.gg.com"
