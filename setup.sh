if [ ! -d output ]; then
  mkdir output
fi

if [ ! -d memery ]; then
  python3 -m venv memery
  source memery/bin/activate
  pip3 install -r requirements.txt
fi

