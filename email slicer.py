
email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
split_name = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(split_name)