

class Subblock():
    def __init__(self, _content, _width:int, _height:int, _position:tuple[int,int]) -> None:
        self.content = _content

class Column(Subblock):
    def __init__(self, _content, _width=None) -> None:
        super().__init__(_content, _width, None, (None,None))

class Floating(Subblock):
    def __init__(self, _content, _position: tuple[int, int], _width: int = None, _height: int = None) -> None:
        super().__init__(_content, _width, _height, _position)
