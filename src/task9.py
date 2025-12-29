from typing import Any


class Person:
    
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value: Any) -> None:
        parts = str(value).strip().split()
        if len(parts) < 2:
            raise ValueError("full_name must include first and last name")
        self.first_name = parts[0]
        self.last_name = " ".join(parts[1:])

    def __repr__(self) -> str:
        return f"Person({self.full_name!r})"


def main() -> None:
    p = Person("John", "Doe")
    print("Создано:", p)
    print("full_name:", p.full_name)

    p.full_name = "Jane Smith"
    print("После смены имени:", p)

    try:
        p.full_name = "SingleName"
    except ValueError as e:
        print("Ожидаемая ошибка при установке некорректного full_name:", e)


if __name__ == "__main__":
    main()
