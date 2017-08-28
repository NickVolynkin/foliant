"""PlantUML processor."""

import subprocess
from os.path import join


PLANTUML_COMMAND = "plantuml"


def process_diagram(caption, body, src_dir, diag_dir_name, diag_id):
    """Save diagram body to .diag file, draw PNG from it with plantuml,
    and return the image ref."""

    diag_src_path = join(src_dir, diag_dir_name, "%s.diag" % diag_id)

    with open(diag_src_path, 'w', encoding="utf8") as diag_src:
        diag_src.write(body)

    try:
        subprocess.check_output(
            "%s %s" % (PLANTUML_COMMAND, diag_src_path),
            stderr=subprocess.PIPE,
            shell=True
        )
    except subprocess.CalledProcessError as exception:
        print("Processing diagram %s failed: %s" % (diag_src_path, exception))

    return "![%s](%s/%s.png)" % (caption, diag_dir_name, diag_id)
