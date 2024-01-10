from abc import ABC, abstractmethod
class IDataObject(ABC):
    @abstractmethod
    def doseExist(self, remoteFilePath : str) -> bool:
        pass
    @abstractmethod
    def upload(self, file : bytearray) -> None:
        pass
    @abstractmethod
    def download(self, remoteFilePath : str, localFilePath : str) -> bytearray:
        pass
    @abstractmethod
    def publish(self, remoteFilePath : str, expirationTime : int = 90) -> str:
        pass
    @abstractmethod
    def remove(self, remoteFilePath : str, recursive : bool = False) -> None:
        pass