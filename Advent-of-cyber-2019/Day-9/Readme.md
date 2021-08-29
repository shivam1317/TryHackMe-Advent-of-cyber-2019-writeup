
--> python script which i made for this task 

```py
import requests 

path = ''
host = 'http://10.10.169.100:3000/'
values = []
while(path != 'end'):
	response = requests.get(host + path)
	json_response = response.json()
	path = json_response['next']
	values.append(json_response['value'])
print("".join(values))	
```

