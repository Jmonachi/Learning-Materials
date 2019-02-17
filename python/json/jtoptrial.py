import json

k = '{"name":"James Bond", "age":30,"city":"Nairobi","Nationality":"Kenyan"}'

l = json.loads(k)

print(l["name"])


