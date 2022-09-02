from dataclasses import dataclass


@dataclass
class Config:
    """Dataclass for configuration of the latex file."""

    doc_class: str
    doc_font: str
    font_size: int
    margin: int
    paper_size: str
    indent_size: int
    sloppy: bool
    code_font: str
    cfont_scale: float
    code_conf: str
    packages: list[str]
    footnote: str
    section_sizes: dict[str, int | str]
    links: bool
    link_color: str
    author: str
    date: str
    make_title: bool
    output_folder: str
    compiler: str
    encode: str


@dataclass(frozen=True)
class Rules:
    """Dataclass for configuration of the parser."""

    files: list[str]
    code: str
    image: str
    links: str
    section: str
    sectionn: str
    subsection: str
    subsectionn: str
    subsubsection: str
    subsubsectionn: str
    paragraph: str
    paragraphn: str
    subparagraph: str
    subparagraphn: str
    inline_math: list[str]
    paragraph_math: str
    inline_code: list[str]
    bold: list[str]
    italics: list[str]
    emph: list[str]
    strike: list[str]
    supscript: list[str]
    subscript: list[str]
    uline: list[str]
    quote: list[str]
    bquote: str
