import re


def process_includes(content):
    include_statement = re.compile(
        r"\{\{\s*(<(?P<repo>.+)\>)?" +
        r"(?P<path>.+?)(\#(?P<from_heading>.+?)(:(?P<to_heading>.+?))?)?" +
        r"\s*(\|\s*(?P<options>.+))?\s*\}\}"
    )

    for include in re.finditer(include_statement, content):
        print("---------------------")
        print("Repo: %s" % include.group("repo"))
        print("Path: %s" % include.group("path"))
        print("From heading: %s" % include.group("from_heading"))
        print("To heading: %s" % include.group("to_heading"))

        options = include.group("options")

        if options:
            for option in options.split(","):
                print("Option: %s" % option.strip())

    return content


if __name__ == "__main__":
    process_includes("""This is a sample that includes an include statement:

{{ <myrepo>/path/to/file.md#heading1:heading2 | nohead, sethead:3 }}

Another one:

{{../path/to/file.md#heading1}}

Here's some text after it.
""")
