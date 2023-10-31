# AMI Windows Server with IIS

This project bakes Windows server with IIS enabled via Packer using EC2 spot instances.

## Build the project

1. Add your aws account and infrastructure details to `ami-windows-iis-webserver.json`
2. Build the AMI `packer build ami-windows-iis-webserver.json`
3. Add the new ami id to `create_windows_iis_webserver.py`
4. Create a new virtualenv folder `virtualenv .venv`
5. Activate virtualenv and install `boto3`
  - `source virtualenv/bin/activate`
  - `pip3 install boto3`
6. Start a new EC2 instance using the script `python3 create_windows_iis_webserver.py`

Check the new EC2 instance in the EC2 dashboard, and connect to via browser `http://<ec2-elastic-ip>:80`

