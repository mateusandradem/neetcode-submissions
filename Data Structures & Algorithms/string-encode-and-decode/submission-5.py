class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return 'None'
        return '+{}{0}°'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s is 'None':
            return []
        return s.split('+{}{0}°')