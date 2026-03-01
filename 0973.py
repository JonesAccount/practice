numbers = [1, 2, 3, 4, 5]
info = {"name": "Alice", "city": "Moscow"}


def process_data(*args, **kwargs) -> str:
    for k, v in kwargs.items():
        print(f"{k} = {v}")
    
    d = {}
    d["sum"] = sum(args)
    d["count"] = len(args)
    print(d)

result = process_data(*numbers, **info)