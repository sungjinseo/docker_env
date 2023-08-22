c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.notebook_dir = '/home/jupyter'
c.NotebookApp.allow_origin = '*'
#c.NotebookApp.token = ''
# 보안 위협에 노출 될 수 있으므로 반드시 password를 설정합니다. (sha)
c.NotebookApp.password = 'sha1:b00ee0c0e13c:9b3f0c11356d567b4b9c516af4aeae5df5a2f1e4'