#!/usr/bin/python2
import sys
import xmlrpclib
import datetime

class Package(object):
    client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
    
    def get_package(self, package_name, version=None):
        if version is None:
            versions = self.client.package_releases(package_name)
            version = versions[-1]
        self.version = version
        
        data = self.client.release_data(package_name, version)
        urls = self.client.release_urls(package_name, version)[0]
        
        pyversion = urls['python_version']
        if pyversion in ('source', 'any'):
            self.pyversion = 'python2'
        if pyversion.startswith('3'):
            self.pyversion = 'python'
        else:
            self.pyversion = 'python2'
        
        self.name = data['name']
        self.description = data['summary']
        self.download_url = urls['url']
        self.md5 = urls['md5_digest']
        self.url = data.get('home_page', '')
        self.license = data['license']
    
    def render(self):
        with open('blank_pkgbuild') as f:
            strn = f.read()
        return strn.format(pkg=self, date=datetime.date.today())


if __name__ == '__main__':
    
    package_name = sys.argv[1] if len(sys.argv) > 1 else sys.exit('Need package name as first argument')
    
    p = Package()
    p.get_package(package_name)
    with open('PKGBUILD', 'w') as f:
        f.write(p.render())