user_input = input("Enter your username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "';"
print(query)  # This can be exploited
