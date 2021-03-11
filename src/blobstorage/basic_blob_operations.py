from azure.storage.blob import BlobServiceClient

blob_client_connstr = ""  # connection string of target storage account


def read_blob_file(container_name=None, blob_name=None, target_path=None):
    """
    read_blob_file reads a single blob from azure storage account containr

    Parameters:
    -----------
    container_name: str
        name of the container(default:None)
    blob_name: str
        name of the blob to read(default:None)
    target_path: str
        absolute local file path to store blob(default:None)

    Returns:
    --------
    op_status: bool
        a boolean value indicating status of read operation.

    Raises:
    -------
    gen_err: Exception
        raised when an unknown exception is caught
    """
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            blob_client_connstr)
        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob=blob_name
        )
        with open(target_path, "wb") as fh:
            blob_data = blob_client.download_blob()
            blob_data.readinto(fh)
        return True
    except Exception as gen_err:
        print(gen_err)
        return False
