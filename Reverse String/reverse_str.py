
def reverse_str(string_to_reverse: str)->str:
    split_string = string_to_reverse.split(" ")
    reversed_str = [x[::-1] for x in split_string]
    return (" ".join(reversed_str))

def test_cases():
    string_1 = " "
    string_2 = "Hello, World!"
    string_3 = "I  "
    assert reverse_str(string_3) == "I  ", f"Error: Received {reverse_str(string_3)}"
    assert reverse_str(string_2) == ",olleH !dlroW", f"Error: Received {reverse_str(string_2)}"
    assert reverse_str(string_1) == " ", f"Error: Received {reverse_str(string_1)}"

if __name__ == "__main__":
    test_cases()