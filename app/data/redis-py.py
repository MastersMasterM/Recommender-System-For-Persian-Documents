import redis
import json

r = redis.Redis(db=2,host='redis', port=6379)

"""recom_list = np.load('/home/m4ster/Desktop/Thesis-Platform/app/data/small-sbert.npy')

def select_top_k(k:int, df:pd.DataFrame, threshold:float=0.8) -> dict[int,list[int]]:

  #Filter the recommend object
  df = df.applymap(lambda x: x if x >= threshold else -10)
  res_index = df.apply(lambda row: [idx for idx, val in row.nlargest(k).items() if val != -10], axis=1).to_dict()

  return res_index

res = select_top_k(5, pd.DataFrame(recom_list))
dumped = json.dumps(res)
with open('/home/m4ster/Desktop/Thesis-Platform/app/data/list.json', 'w') as f:
  f.write(dumped)
"""

with open('data/list.json', 'r') as f:
    res = json.load(f)

my_dict_bytes = {k:json.dumps(v).encode('utf-8') for k,v in res.items()}

r.mset(my_dict_bytes)
