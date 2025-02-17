from abc import abstractmethod, ABC


class IS3ClientWrapper(ABC):
    @abstractmethod
    def download_file(self, bucket: str, s3_path: str, dest_filename: str) -> None:
        pass
    class S3ClientWrapper(IS3ClientWrapper):
    def __init__(self, s3_client):
        self.s3_client = s3_client

    def download_file(self, bucket: str, s3_path: str, dest_filename: str):
        self.s3_client.download_file(bucket, s3_path, dest_filename)
class S3ClientWrapper(IS3ClientWrapper):
    def __init__(self, s3_client):
        self.s3_client = s3_client

    def download_file(self, bucket: str, s3_path: str, dest_filename: str):
        self.s3_client.download_file(bucket, s3_path, dest_filename)
class TestS3ClientWrapper(IS3ClientWrapper):

    def download_file(self, bucket: str, s3_path: str, dest_filename: str):
        Path(dest_filename).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(s3_path, dest_filename)
        from abc import abstractmethod, ABC


class IS3ClientWrapper(ABC):
    @abstractmethod
    def download_file(self, bucket: str, s3_path: str, dest_filename: str) -> None:
        pass


class S3ClientWrapper(IS3ClientWrapper):
    def __init__(self, s3_client):
        self.s3_client = s3_client

    def download_file(self, bucket: str, s3_path: str, dest_filename: str):
        self.s3_client.download_file(bucket, s3_path, dest_filename)
