from fabric.api import env, run, sudo, cd
from fabric.contrib.files import exists

try:
    import fabsecrets
except ImportError:
    raise ImportError('Did you edit fabsecrets_template.py and rename it to fabsecrets?')

env.project_repository_uri = 'https://github.com/Ateoto/ateoto.com.git'
env.deploy_dir = '/home/ubuntu/sites/ateoto.com'
env.virtualenv = 'ateoto.com'
env.hosts = ['ubuntu@ateoto.com']

def install_packages():
	sudo('apt-get update')
	sudo('apt-get install -y nginx')
	sudo('apt-get install -y postgresql')
	sudo('apt-get install -y git')
	sudo('apt-get install -y virtualenvwrapper')

	"""
	Still have to setup nginx and postgresql
	"""

def update_code():
	if not exists(env.deploy_dir):
		run('git clone %s %s' % (env.project_repository_uri, env.deploy_dir))
	else:
		with cd(env.deploy_dir):
			run('git pull')

def provision():
	"""
	Set up directories and files on server. Installs necessary apps.
	This currently is set up for Ubuntu.
	"""

	install_packages()
	update_code()
