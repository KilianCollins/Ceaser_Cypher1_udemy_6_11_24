import time


def connect() -> None:
    print("Connecting ... ")
    time.sleep(3.0)
    print("Connected!")

if __name__ == "__main__":
    # what does __name__ d0? --k 6_11_24
    connect()