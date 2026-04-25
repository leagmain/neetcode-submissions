class Solution:

    def __init__(self):
        self.SEP = chr(260)
        self.EMPTY = chr(271)
        self.NONE = chr(272)

    def encode(self, strs: List[str]) -> str:
        # strs might be empty
        if len(strs) == 0:
            return self.EMPTY
        return self.SEP.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.EMPTY:
            return []
        return s.split(self.SEP)
