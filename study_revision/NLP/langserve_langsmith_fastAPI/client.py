# import requests

# # response=requests.post(
# #     "http://localhost:8000/math/invoke",
# #     json={'input':{'input':"9x+10=80"}})

# pickup_response=requests.post(
#     "http://localhost:8000/pickup/invoke",
#     json={'input':{'input':"movie"}})


# # print(response.json())
# print(pickup_response.json())
# # print(response.json()['output']['content'])


import requests

# Request to test the math route:
math_response = requests.post(
    "http://localhost:8000/math/invoke",
    json={'input': "9x+10=80"}
)

# Request to test the pickup line route:
pickup_response = requests.post(
    "http://localhost:8000/pickup/invoke",
    json={'input': "movie"}
)

# Print the responses
print(math_response.json())
# print("Pickup Line Response:", pickup_response.json())
