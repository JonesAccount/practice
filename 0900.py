import json

data = {
        "aiqo": 110,
        "name": "Misha",
        "score": 0,
        "human": True,
        "hobby": ["Programming", "Math", "AI"],
        "hero": None
        }

data_json = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
print(data_json)

data2 = "name: Philip"
data_json_load = json.loads(data2)