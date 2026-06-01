"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""
import requests

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("=== Basic API Request ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())

# Exercise 1: Change the URL to fetch post number 5
#             Hint: Change /posts/1 to /posts/5

url = "https://jsonplaceholder.typicode.com/posts/5"
response=requests.get(url)
print("\n=== Exercise 1: Fetch Post Number 5 ===\n")
print(f"URL:{url}")
print(f"status code:{response.status_code}")
print(f"\nResponse Data:")
print(response.json())

# Exercise 2: Fetch a list of all users
#             URL: https://jsonplaceholder.typicode.com/users

url = "https://jsonplaceholder.typicode.com/users"
response =requests.get(url)
print("\n=== Exercise 2: Fetch the data ===\n")
print(f"URL:{url}")
print(f"status code:{response.status_code}")
print(f"\nResponse Data:")
print(response.json())

# Exercise 3: What happens if you fetch a post that doesn't exist?
#            Try: https://jsonplaceholder.typicode.com/posts/999

url= "https://jsonplaceholder.typicode.com/posts/999"
response=requests.get(url)
print("\n=== Exercise 3: Fetch Post Number 999 ===\n")
print(f"URL:{url}")
print(f"status code:{response.status_code}")
print(f"\nResponse Data:")
print(response.json())

#Exersise 4: operations on json data
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
users = response.json()
print("\n===  Print Usernames ===\n")
for user in users:
    print(user["name"])

print("\n===  Print Usernames ===\n")
for email in users:
    print(email["email"])

print("\n===  print user Details ===\n")
for user in users:
    print(user["name"],"-",user["address"]["city"])

print("\n===  count total users ===\n")
print("total users:",len(users))

print("\n===  print users name in upper ===\n")
for user in users:
    print(user["name"].upper())

for user in users:
    print(user["email"].upper())

for user in users:
    print(user["website"])
print()

for user in users:
    print("id",user["id"])
    print("name",user["name"])
    print("email",user["email"])
    print("city",user["address"]["city"])
    print("-" * 30)

for user in users:
    if user["address"]["city"] == "Gwenborough":
        print(user["name"])

sorted_users = sorted(users, key=lambda user: user["name"])
for user in sorted_users:
    print(user["name"])

emails = [user["email"] for user in users]
print(emails)

longest = max(users, key=lambda user: len(user["username"]))
print(longest["username"])

for user in users:
    print(f"""
    ID      : {user['id']}
    Name    : {user['name']}
    Email   : {user['email']}
    City    : {user['address']['city']}
    Website : {user['website']}
    """)

search_name = input("Enter name: ")

for user in users:
    if search_name.lower() in user["name"].lower():
        print(user)
print("----------------------------------------------")
cities = {}

for user in users:
    city = user["address"]["city"]

    if city in cities:
        cities[city] += 1
    else:
        cities[city] = 1

        print(cities)