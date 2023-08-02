def email_slicer(email):
    # Split the email address at the '@' symbol
    username, domain = email.split('@')

    # Return the username and domain separately
    return username, domain


if __name__ == "__main__":
    # Get the email address from the user
    user_email = input("Enter your email address: ")

    # Call the email_slicer function to get the username and domain
    username, domain = email_slicer(user_email)

    # Print the results
    print("Username:", username)
    print("Domain:", domain)
