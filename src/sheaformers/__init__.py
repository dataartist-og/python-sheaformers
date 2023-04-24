__version__ = "0.0.0"
try:
    from ._sheaformers import longest
except ImportError:

    def longest(args):
        return max(args, key=len)
