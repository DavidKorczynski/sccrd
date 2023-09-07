import atheris
import sys


def target1(s1):
    if len(s1) < 10:
        return
    if s1[0] != 'A':
        return

    print("Hi %d"%(s1[len(s1)*2]))

def TestOneInput(b):
    fdp = atheris.FuzzedDataProvider(b)
    target1(fdp.ConsumeString(100))

def main():
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
