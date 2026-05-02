# build_files.sh
pip install -r requirements.txt --break-system-packages
python3 manage.py collectstatic --noinput --clear