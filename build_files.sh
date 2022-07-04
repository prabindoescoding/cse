# build_files.sh
pip install pysqlite3
pip install -r requirements.txt
python3.9 manage.py collectstatic