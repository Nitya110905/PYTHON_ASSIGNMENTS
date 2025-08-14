# How do you perform pattern matching in Python? Explain.

# - The basic structure consists of a match statement that takes a subject (the value to be matched) followed by one or more case blocks. Python checks the subject against the pattern in each case block from top to bottom. The first one that matches is executed.


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _: # Wildcard pattern
            return "Unknown status"

print(http_status(200)) 
print(http_status(418)) 