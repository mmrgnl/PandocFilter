from panflute import *
import sys

headers = []


def bold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))


def duplicate(elem, doc):
    if type(elem) == Header:
        header = stringify(elem)
        if header in headers:
            print("Duplicate header " + header, file=sys.stderr)
        else:
            headers.append(header)


def upper(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.upper()


def upperHeads(elem, doc):
    if type(elem) == Header and elem.level <= 3:
        return elem.walk(upper)


def main(doc=None):
    return run_filters([duplicate, upperHeads], finalize=bold, doc=doc)


if __name__ == "__main__":
    main()
