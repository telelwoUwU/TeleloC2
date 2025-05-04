from src.cnc import start as start_cnc

if __name__ == '__main__':
    try:
        start_cnc()
    except Exeption as e:
        print("Error, skipping.{e}")
