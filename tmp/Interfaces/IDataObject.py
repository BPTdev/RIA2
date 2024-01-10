class IDataObject:
    def __init__(self) -> None:
        pass
    
    def doesObjectExist(self) -> bool:
        raise NotImplementedError
    
    def uploadObject(self, file: any, remoteFullPath: str) -> None:
        raise NotImplementedError
    
    def downloadObject(self, file, remoteFullPath: str) -> any:
        raise NotImplementedError
    
    def publishObject(self, remoteFullPath: str, expirationTime = 90)-> str:
        raise NotImplementedError
    
    def removeObject(self, remoteFullPath: str) -> None:
        raise NotImplementedError