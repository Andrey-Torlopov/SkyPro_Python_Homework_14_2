#!/bin/zsh

echo "Create python env"
python3 -m venv env

echo "Create config and requirements"
cp ./boot_source/pyvenv.cfg ./env/
cp ./boot_source/requirements.txt ./env/

echo "Start env"
./env/bin/activate

echo "Install requirements"
pip3 install -r ./env/requirements.txt

echo "Done"