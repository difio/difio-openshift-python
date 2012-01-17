from distutils.core import setup

setup(
    name='monupco-openshift-express-python',
    version='1.2',
    description='monupco.com client for OpenShift Express / wsgi-3.2 applications',
    author='Alexander Todorov',
    author_email='atodorov@nospam.otb.bg',
    url='http://monupco.com/',
    download_url='https://github.com/monupco/monupco-openshift-express-python/downloads'
    keywords = ['openshift', 'monupco', 'updates', 'cloud'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems administration",
        ],
    long_description = """
monupco.com client for OpenShift Express / wsgi-3.2
--------------------------------------------------------

This is a client side agent for monupco.com. It compiles
a list of locally installed Python packages and sends it to
monupco.com.


Installing on your OpenShift application
----------------------------------------

Create an account at <http://monupco.com>

Create a wsgi-3.2 application on OpenShift

    rhc-create-app -a myapp -t wsgi-3.2

Add a dependency in your setup.py file

    from setuptools import setup

    setup(
        name='MyApplication',
        version='1.0',
        install_requires=['monupco-openshift-express-python'],
     )

Set your username and application name in the ./data/MONUPCO_SETTINGS file

    echo "export MONUPCO_USERNAME='YourUserName'"  >  ./data/MONUPCO_SETTINGS
    echo "export MONUPCO_APP_NAME='MyApplication'" >> ./data/MONUPCO_SETTINGS

Then push your application to OpenShift

    git push

That's it, you can now checkout your application statistics at:
<http://monupco.com>
"""
     )
