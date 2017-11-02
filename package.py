import pip

PACKAGES = ['requests']

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
	for package in PACKAGES:
		install(package)