"""Everything holds 1000 values; events selectively update one value."""
class EPC:
    def __init__(self, size=1000):
        self.values = [10] * size
        self.calculations = 0
        self.last_position = None
    def something(self, position, index):
        if not isinstance(position, int) or isinstance(position, bool) or position < 1:
            raise ValueError("Invalid position")
        if self.last_position is not None and position <= self.last_position:
            raise ValueError("Events must be ordered")
        if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < len(self.values):
            raise ValueError("Invalid index")
        self.values[index] *= 2
        self.calculations += 1
        self.last_position = position
    @property
    def everything(self):
        return tuple(self.values)
def test():
    e = EPC()
    e.something(1, 417)
    e.something(1_000_002, 417)
    assert e.values[417] == 40
    assert all(v == 10 for i,v in enumerate(e.values) if i != 417)
    assert e.calculations == 2
    print("All 1,000-value EPC tests passed.")
    print("999 values unchanged; calculations=2; million zeros skipped.")
if __name__ == "__main__":
    test()
