#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    aux = dir(hidden_4)
    for item in aux:
        if item[:2] != "__":
            print(item)
