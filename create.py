import sys
import os

projname = str(sys.argv[1])
cwd = os.getcwd() 
dir = cwd + '\\' + projname
try:

	os.system('laravel new ' + projname)
	os.chdir(dir) 
	
	os.system('composer install')
	os.system('npm install vue --save ')
	os.system('npm install vuex --save')
	
	os.system('composer require laravel/ui')
	os.system('php artisan ui bootstrap')
	
	os.system('npm install')
	os.system('npm run dev')
	
	os.system('code .')
	
	os.system('php artisan key:generate')
	os.system('php artisan serve')
	
except:
    print("create <project_name> l")
