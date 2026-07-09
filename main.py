def get_status_message() -> str:
    return "Phase 10 Git CI project is running"


def main() -> None:
    message = get_status_message()
    print(message)


if __name__ == "__main__":
    main()
