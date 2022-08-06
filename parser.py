import csv
import struct
from functools import partial
from typing import Dict
from typing_extensions import Literal, Protocol

LEGACY: Literal["L"] = "L"
ACTUAL: Literal["A"] = "A"
StyleKeyType = Literal["L", "A"]
STYLES: Dict[StyleKeyType, str] = dict((
    (LEGACY, "I8s16s"),
    (ACTUAL, "I32s256s")
))

DEFAULT_LASTLOG = "/var/log/lastlog"
DEFAULT_STYLE = ACTUAL


class BinaryReadable(Protocol):
    """Represent a bianry reader file."""
    def read(self, size: int) -> bytes:
        ...


class TextWritable(Protocol):
    """Represent a text writer file."""
    def write(self, data: str) -> int:
        ...


def lastlog_to_csv(
    lastlog_in: BinaryReadable,
    csv_out: TextWritable,
    style: StyleKeyType = DEFAULT_STYLE
) -> None:
    """Convert an lastlog input stream to an csv output stream."""
    fmt = STYLES[style]
    structure = struct.Struct(fmt)
    writer = csv.writer(csv_out, lineterminator="\n")
    for block in iter(partial(lastlog_in.read, structure.size), b""):
        if any(block):
            timestamp: int
            line: bytes
            host: bytes
            timestamp, line, host = structure.unpack(block)
            writer.writerow((timestamp,
                             line.rstrip(b"\x00").decode("utf8"),
                             host.rstrip(b"\x00").decode("utf8")))
