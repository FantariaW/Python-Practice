# Day 6 Training: class, assert, isinstance

# Day 6 Training
class EmployeeCard:
    @staticmethod
    def is_int(num: str) -> bool:
        """
        test function for testing numeric value
        :param num: str - user input value
        :return: int - numeric value
        """
        try:
            new_num = int(num)
            return isinstance(new_num, int)
        except ValueError:
            return False

    def get_prompt(self, prompt_name: str, prompt_year: str):
        """
        prompt the user to enter name and year
        :param prompt_name: str - user's name
        :param prompt_year: int user's year
        :return: name: year
        """

        employee_lst = []

        print("==Employee Information==")
        print("--Please enter name and year--")

        while True:
            try:
                name = input(prompt_name).strip()
                if name.lower() == 'done':
                    break

                assert name != "", "Name can't be space!"
                assert name.isalpha(), f"Name: {name} is invalid! must be alphabetic!"

                while True:
                    try:
                        year = input(f"{name.title()}{prompt_year}").strip()

                        assert year != "", "Year can't be space!"
                        assert self.is_int(year), f"Year: {year} is invalid! must be numeric!"
                        year = int(year)
                        assert int(year) >= 0, f"Year: {year} must be positive numeric value!"

                        employee_dict = {
                            "name": name.title(),
                            "year": int(year)
                        }
                        employee_lst.append(employee_dict)
                        print(f"✅Employee {name.title()} ({year} years) Logged in successfully!", end="\n\n")

                        break
                    except (ValueError, AssertionError) as e:
                        print(e)
            except (ValueError, AssertionError) as e:
                print(e)

        return employee_lst

    @staticmethod
    def employee_tbl(emp_lst):
        result = ["== Employee Info Table =="]

        for each_emp_dict in emp_lst:
            emp_name = each_emp_dict['name']
            emp_year = each_emp_dict['year']

            result.append(f"- {emp_name}: {emp_year} years.")

        return "\n".join(result)


def main():
    """
    main function use to test the whole program, will not import in other file.
    :return: run and test whole program
    """
    prompt_name = "Name: "
    prompt_year = "\'s Year: "
    card = EmployeeCard()
    card_tbl = EmployeeCard()

    employee_lst = card.get_prompt(prompt_name, prompt_year)
    employee_tbl = card_tbl.employee_tbl(employee_lst)

    print(employee_lst, "\n")  # only use for debug
    print(employee_tbl)  # whole program output


if __name__ == "__main__":
    main()
