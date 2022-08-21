from shutil import copy
from os import mkdir
from os.path import exists
from typing import TextIO

from src.config import Config, Rules
from src.utils.tex.sections.headings import headings
from src.utils.tex.sections.body import body
from src.mutils.format_body import format_body
from src.utils.logger import Logger


def convert(
        log: Logger,
        rules: Rules,
        config: Config,
        title: str,
        in_file: str,
        filenametitle: bool
    ) -> None:
    """This unifies all the modules.

    Args:
        log -- for logging.
        rules -- rules that needs to be followed in translation.
        config -- configuration of the document metadata, which includes,
            formatting, packages to use among others, refer to simtex.json.
        title -- title of the document.
        in_file -- path of the file to be converted to LaTeX.
    """

    log.logger("I", f"Converting {in_file} ...")

    OFILE_PATH: str
    if exists((OFILE_PATH := f"{config.output_folder}/{config.filename}")):
        if input(
                (
                    f"\033[1mINPT\033[0m\t File: {OFILE_PATH}"
                    " already exists, overwrite? "
                )
            ).lower() != "y":
            log.logger(
                "e", f"File: {OFILE_PATH} already exists, aborting ..."
            )
            raise SystemExit

    if not exists(config.output_folder):
        log.logger("I", f"Creating dir: {config.output_folder} ...")
        mkdir(config.output_folder)

    if filenametitle and title is None:
        title = in_file.split("/")[-1].split(".")[0]
    else:
        if input(
                (
                    "\033[1mINPT\033[0m\t Title is"
                    " none, use filename as title? "
                )
            ).lower() == "y":
            title = in_file.split("/")[-1].split(".")[0]
        else:
            title = input("\033[1mINPT\033[0m\t Input title for use: ")

        log.logger(
            "I", f"Title is none, using filename: {title} as title ..."
        )

    if in_file.startswith("./"):
        OPATH = "/".join(in_file.split("/")[:-1])
    else:
        OPATH = "./"+"/".join(in_file.split("/")[:-1])

    out_file: TextIO
    with open(OFILE_PATH, "w", encoding="utf-8") as out_file:
        start: int = headings(log, config, title, out_file)
        files: list[str] = body(log, rules, in_file, out_file)

    format_body(log, config, start, OFILE_PATH)

    file: str
    for file in files:
        log.logger("I", f"Copying {file} into {config.output_folder} ...")
        filename: str = file.split("/")[-1]
        try:
            copy(
                f"{OPATH}/{file.replace('./', '')}",
                f"{config.output_folder}/{filename}"
            )
        except (FileNotFoundError, OSError, IOError) as Err:
            log.logger(
                "e", f"Encountered: {Err} while moving {file}, skipping"
            )
