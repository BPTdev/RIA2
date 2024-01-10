class ILabelDetector():
    def __init__(self) -> None:
        pass
    def analyse(remotePath: str, maxLabels: int = 10, minConfidenceLevel: float = 90) -> any:
        raise NotImplementedError