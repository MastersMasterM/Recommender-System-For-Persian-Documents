import redis
import json

r = redis.Redis(db=2, host='redis', port=6379)

with open('data/list.json', 'r') as f:
    res = json.load(f)

my_dict_bytes = {k: json.dumps(v).encode('utf-8') for k, v in res.items()}

r.mset(my_dict_bytes)
