import logging

from azureml.core import (
    Workspace,
    Experiment,
    Environment,
    ScriptRunConfig
)
azureml_config_path = ""
ws = Workspace.from_config(azureml_config_path)
experiment_obj = Experiment(workspace=ws, name="<experiment name>")

def run_random_experiment(script_name:str) -> str:
    try:
        env_obj = Environment("custom_docker_environment")
        env_obj.docker.base_image_registry = ""
        env_obj.docker.base_image_registry.username = "" # to be pulled from azure keyvault
        env_obj.docker.base_image_registry.password = "" # to be pulled from azure keyvault
        config = ScriptRunConfig(
            source_directory="<>", 
            script="<>", 
            compute_target="<cluster_name>")
        config.run_config.environment = env_obj
        run_instance = experiment_obj.submit(config)
        aml_url = run_instance.get_portal_url()
        return aml_url
    except Exception as err:
        logging.error(err)



def main():
    # put selected modules here
    pass

if __name__ == '__main__':
    main()