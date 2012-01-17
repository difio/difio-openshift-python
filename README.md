monupco.com client for OpenShift Express / wsgi-3.2
========================================================

This git repository helps you set up and running a monupco.com
client for wsgi-3.2 types of applications hosted on OpenShift Express.

Installing in your OpenShift application
--------------------------------------------------------

Create an account at <http://monupco.com>

Create a wsgi-3.2 application on OpenShift

    rhc-create-app -a myapp -t wsgi-3.2

Add this upstream repo

    cd myapp
    git remote add monupco -m master https://bitbucket.org/atodorov/monupco-openshift-express-python.git
    git pull -s recursive -X theirs monupco master

Set your username and application package name in the ./data/MONUPCO_SETTINGS file

    echo "export MONUPCO_USERNAME='YourUserName'"  >  ./data/MONUPCO_SETTINGS
    echo "export MONUPCO_APP_PKG='AppPackageName'" >> ./data/MONUPCO_SETTINGS

Then push the application to OpenShift

    git push

That's it, you can now checkout your application statistics at:
<http://monupco.com>


Updating
--------------------------------------------------------

To update the monupco.com client to a later version execute

    git pull monupco master
