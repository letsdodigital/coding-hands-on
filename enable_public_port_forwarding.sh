#!/bin/bash

# You may need to run chmod +x enable_public_port_forwarding.sh to be able to
# run this script

EXIT=0
BB='\033[1;34m'
BR='\033[1;31m'
BG='\033[1;32m'
BP='\033[1;35m'
NC='\033[0m'

PORTS=""
PORTS_VISIBILITY=""

# Change 8501 8530 to range of ports you want to open
for i in $(seq 8501 8530);
do
    PORTS+="$i:$i "
    PORTS_VISIBILITY+="$i:public "
done

printf "${BB}Forwarding codespace ports..${NC}\n"

# Using timeout because command will not exit as it is forwarding ports but
# there no other API to open without using devcontainer.json forwardPorts
# option. 8s is likley long-enough?
timeout 8s gh codespace ports forward $PORTS -c $CODESPACE_NAME

printf "\n${BB}Setting codespace forwarded ports to public..${NC}\n"
gh codespace ports visibility $PORTS_VISIBILITY -c $CODESPACE_NAME
if [ $? -ne 0 ]; then
    printf "\n${BR}Error setting ports visiblity to public.\n"
    printf "Check messages above, review \"ports\" tab and"
    printf " consider running this script again.\n\n"
    printf "Continuing to install +/- patch streamlit${NC}\n"
    EXIT=1
fi

printf "\n${BB}Checking if Streamlit is installed..${NC}\n"
python -c "import streamlit" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    printf "${BP}Streamlit not installed.${NC}"
    printf "${BB} Installing with pip..${NC}\n"
    pip install streamlit
else
    printf "${BG}Streamlit already installed!${NC}\n"
fi

STREAMLIT=$(pip show streamlit | awk '/Location: / { print $2 }')
if [ -z "$STREAMLIT" ]; then
    echo -e "${BR}Unable to determine install location of Streamlit.${NC}" >&2
    exit 1
fi
STREAMLIT_UTILS="$STREAMLIT/streamlit/web/server/server_util.py"

printf "\n${BB}Checking if Streamlit server_util.py already patched..${NC}\n"
MATCH_MOD="    return f\"https:\/\/{codespace_name}-{port}.app.github.dev\/\""
grep -q "$MATCH_MOD" $STREAMLIT_UTILS
if [ $? -eq 0 ]; then
    printf "${BG}Patch found! "
    if [ $EXIT -eq 0 ]; then
        printf "Public ports setup completed successfully!${NC}\n\n"
        exit 0
    else
        printf "${NC}${BR}Public ports setup completed with errors!${NC}\n\n"
        exit 1
    fi
else
    printf "${BP}Streamlit not patched.${NC}\n"
fi

printf "${BB}Checking for correct Streamlit server_util.py version..${NC}\n"
if ! echo "547aba3d2a96920e4777f996443bfedeaafd3f9e $STREAMLIT_UTILS" | 
    sha1sum -c -; then

    printf "${BR}Preparing to patch server_util.py but checksum failed.\n" >&2
    printf "Have you alrady run this script?${NC}\n" >&2
    exit 1
fi

printf "${BB}Patching Streamlit server_util.py..${NC}\n"
MATCH="    return f\\\"{protocol}:\/\/{host_ip}:{port}{base_path}\\\""

PATCH="    #return f\\\"{protocol}:\/\/{host_ip}:{port}{base_path}\\\"\\n\\n"
PATCH+="    import os\n"
PATCH+="    codespace_name = os.environ['CODESPACE_NAME']\n"
PATCH+="    return f\"https:\/\/{codespace_name}-{port}.app.github.dev\/\""

# Final sanity check even though sah1sum check should have stopped us getting
# this far
grep -q "$MATCH" $STREAMLIT_UTILS
if ! [ $? -eq 0 ]; then
    printf "${BR}Failed to patch server_util.py\n" >&2
    printf "Have you alrady run this script?${NC}\n" >&2
    exit 1
fi
sed -i "s/$MATCH/$PATCH/g" $STREAMLIT_UTILS

if [ $EXIT -eq 0 ]; then
    printf "${BG}Public ports setup completed successfully!${NC}\n\n"
    exit 0
else
    printf "${BR}Public ports setup completed with errors!${NC}\n\n"
    exit 1
fi