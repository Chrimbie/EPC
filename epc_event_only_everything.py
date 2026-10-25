"""Something updates persistent Everything; off positions are not processed."""
from dataclasses import dataclass
NOTHING = object()
@dataclass(frozen=True)
class Everything:
    value: object
    calculations: int
class EPC:
    def __init__(self, initial=NOTHING):
        self.value = initial
        self.calculations = 0
        self.last_position = None
    @property
    def everything(self):
        return Everything(self.value, self.calculations)
    def something(self, position):
        if not isinstance(position, int) or isinstance(position, bool) or position < 1:
            raise ValueError("Invalid event position")
        if self.last_position is not None and position <= self.last_position:
            raise ValueError("Events must be ordered")
        if self.value is NOTHING:
            raise ValueError("Nothing is not zero")
        self.value *= 2
        self.calculations += 1
        self.last_position = position
        return self.everything
def test():
    e = EPC(10)
    assert e.something(1) == Everything(20, 1)
    assert e.something(6) == Everything(40, 2)
    huge = EPC(10)
    huge.something(1)
    huge.something(1_000_002)
    assert huge.everything == Everything(40, 2)
    print("All event-only Something-to-Everything tests passed.")
    print("Million-zero gap: Everything=40; calculations=2; no zeros fed.")
if __name__ == "__main__":
    test()
