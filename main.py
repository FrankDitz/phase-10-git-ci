def get_status_message() -> str:
    return "This message should fail CI temporarily"


def main() -> None:
    message = get_status_message()
    print(message)


if __name__ == "__main__":
    main()
