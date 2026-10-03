import argparse

def main():
    parser = argparse.ArgumentParser(prog="issachar")
    parser.add_argument("--version", action="store_true")
    args = parser.parse_args()
    if args.version:
        from . import __version__
        print(__version__)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
