import json 

# dumps() = This is used to convert python object into json string. 

dict1 = {"Name":"Harshil", "Age":24, "Male":True}

print("Python Dict: ",dict1, " Type: ",type(dict1))

result = json.dumps(dict1)

print("Result: ",result, "Type: " ,type(result))


print("\n====================\n")


# loads() = Ths is used to convert json string into python object.

json_data = '{"Name":"Harshil", "Age":24, "Male":true}'

print("Json Data: ", json_data, "Type: ", type(json_data))

new_result = json.loads(json_data)

print("Result: ", new_result, "Type: ", type(new_result))