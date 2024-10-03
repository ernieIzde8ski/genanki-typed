from collections.abc import Iterator
from sqlite3 import Cursor

from ._types import BaseModel


class Card(BaseModel):
  ord: int
  suspend: bool = False

  def write_to_db(
    self,
    cursor: Cursor,
    timestamp: float,
    deck_id: int,
    note_id: int,
    id_gen: Iterator[int | None],
    due: int = 0,
  ):
    queue = -1 if self.suspend else 0
    # fmt: off
    cursor.execute(
      "INSERT INTO cards VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",
      (
        next(id_gen),    # id
        note_id,         # nid
        deck_id,         # did
        self.ord,        # ord
        int(timestamp),  # mod
        -1,              # usn
        0,               # type (=0 for non-Cloze)
        queue,           # queue
        due,             # due
        0,               # ivl
        0,               # factor
        0,               # reps
        0,               # lapses
        0,               # left
        0,               # odue
        0,               # odid
        0,               # flags
        "",              # data
      ),
    )
    # fmt: on
