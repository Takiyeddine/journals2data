with open(
        filepath, encoding = 'utf-8', mode = 'a+'
    ) as file:
        spaces: str = "    "

        file.write(spaces + str(self) + endl)