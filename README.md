monupco.com client for OpenShift Express / wsgi-3.2
========================================================

This git repository helps you set up and running a CloudBerry
client for wsgi-3.2 types of applications hosted on OpenShift Express.

Installing in your OpenShift application
--------------------------------------------------------

Create an account at <http://monupco.com>

Create a wsgi-3.2 application on OpenShift

    rhc-create-app -a myapp -t wsgi-3.2

Add this upstream repo

    cd myapp
    git remote add cloudberry -m master https://bitbucket.org/atodorov/cloudberry-openshift-express-python.git
    git pull -s recursive -X theirs cloudberry master

Set your username and application package name in the ./data/CLOUDBERRY_SETTINGS file

    echo "export CLOUDBERRY_USERNAME='YourUserName'"  >  ./data/CLOUDBERRY_SETTINGS
    echo "export CLOUDBERRY_APP_PKG='AppPackageName'" >> ./data/CLOUDBERRY_SETTINGS

Then push the application to OpenShift

    git push

That's it, you can now checkout your application statistics at:
<http://monupco.com>


Updating
--------------------------------------------------------

To update the CloudBerry client to a later version execute

    git pull cloudberry master
