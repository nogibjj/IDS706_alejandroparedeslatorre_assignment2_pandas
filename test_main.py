from main import print_custom_message


def test_add():
    """Testing that function"""
    assert (
        print_custom_message("Alejandro", 2000, 2, 5)
        == "Hello Alejandro, you are 24 years old and 6 months"
    )
    print("Success")


if __name__ == "__main__":
    test_add()
