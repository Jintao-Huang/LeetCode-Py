import os
import unittest as ut


class TestML(ut.TestCase):
    def test_ml(self):
        fnames = os.listdir("answer")
        for fname in fnames:
            fpath = os.path.join("answer",  fname)
            if os.path.isfile(fpath):
                os.system(f"python {fpath}")


if __name__ == "__main__":
    ut.main()
