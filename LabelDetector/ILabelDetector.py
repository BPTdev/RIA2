from abc import ABC, abstractmethod
class ILabelDetector(ABC):
    @abstractmethod
    def analyze(self, remoteFilePath : str, maxLabels : int = 10, minConfidenceLevel : float = 90) -> str:
        pass