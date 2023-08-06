_other_installs () {
    if [[ $REQUIRMENTS != "None" ]]; then
        apt install $REQUIRMENTS -y
    fi
}

_externals () {
    if [[ $RUN_CMD != "None" ]]; then
        $RUN_CMD
    fi
}

apt update && apt upgrade -y
apt install git -y
_other_installs
pip3 install -U pip
git clone $PRIVATE_REPO_URL Github_Repo
cd Github_Repo
pip3 install -U -r requirements.txt
_externals
python3 $FILE_PATH
