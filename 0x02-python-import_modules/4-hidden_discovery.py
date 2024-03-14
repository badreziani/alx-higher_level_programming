#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    names = [name for name in names if name[:2] != "__"]
    for name in names:
        print(name)
