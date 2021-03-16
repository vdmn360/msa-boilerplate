FROM mcr.microsoft.com/azureml/base:openmpi3.1.2-ubuntu18.04
COPY . app/
RUN bash app/setup_pyodbc_ubuntu.sh
RUN bash app/setup_python3_dev.sh
RUN pip install --no-cache-dir azureml-defaults
RUN pip install -r app/requirements.txt
