# Day 6 Training: assert

# Day 6 Training 1:
def login(user_name: str, password: str) -> str:
    assert user_name != "", "Please enter user name!"
    assert len(password) >= 6, "At least 6 characters!"

    if user_name.lower() == 'admin' and password == "123456":
        return "Login Successfully!"
    return "User name or password wrong!"


def float_num(a, b):
    try:
        float(a)
        float(b)
        return True
    except ValueError:
        return False


# 更嚴格的判定數字，整數，小數
def is_numeric(value) -> bool:
    return isinstance(value, (int, float))


# Day 6 Training 2:
def safe_divide(a, b):
    assert b != 0, "Divisor 'b' can't be 0"
    assert float_num(a, b), "'a' and 'b' must be numeric!"
    assert is_numeric(a) and is_numeric(b), "'a' and 'b' must be numeric!"
    return a / b


def main():
    # login("", "123")
    # login("admin", "123")
    print(login("admin", "123456"))

    # safe_divide(10, 0)
    # safe_divide("10",1)
    print(safe_divide(10, 5))


if __name__ == "__main__":
    main()
