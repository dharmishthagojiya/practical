import json
#json to python object
x='{"name":"dhara","age":20,"city":"rajkot"}'
y=json.loads(x)
print(y["name"])
#python object to json
y1={"a":100,"b":20,"c":80,"d":90}
ptoj=json.dumps(y1)
print(ptoj)
#Python program to convert Python objects into JSON string
print(json.dumps([1,2,3,4]))
print(json.dumps((10,20,30)))
print(json.dumps({1:10,2:30,3:40}))
print(json.dumps("hello"))
print(json.dumps(10.3))
print(json.dumps(None))
print(json.dumps({2:400,1:20,00:89,0:100},indent=10,sort_keys=True))
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(python_obj)
json_obj = json.loads(python_obj)
print("\nUnique Key in a JSON object:")
print(json_obj)
