def is_called():
    def is_returned():
        print("Good Morning")
    return is_returned


new = is_called()

# Outputs "Hello"
new()

