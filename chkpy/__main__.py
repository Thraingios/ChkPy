'''
Author(s): Nick
Created date: 12/3/21
Description: main call for chkpy
last edit: 12/3/21
'''
import sys
from main import main as mymain


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    try:
        mymain(args)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())
