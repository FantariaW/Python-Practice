def name_length(prompt_name, validate_function, error_msg):
    while True:
        try:
            name = input(prompt_name).strip()
            assert validate_function(name), error_msg
            return name
        except AssertionError as e:
            print(e)


user_name = name_length(
    "What's your name: ",
    lambda n: len(n) >= 2,
    "Name length must longer than 2!"
)
