CloudBerry client for OpenShift Express / wsgi-3.2
========================================================

This git repository helps you set up and running a CloudBerry
client for wsgi-3.2 types of applications hosted on OpenShift Express.

Installing on OpenShift
--------------------------------------------------------

Create an account at <http://cvmon-otb.rhcloud.com>

Create a wsgi-3.2 application on OpenShift

    rhc-create-app -a myapp -t wsgi-3.2

Add this upstream repo

    cd myapp
    git remote add cloudberry -m master https://bitbucket.org/atodorov/cloudberry-openshift-express-python.git
    git pull -s recursive -X theirs cloudberry master

Then push the repo to OpenShift

    git push

That's it, you can now checkout your application statistics at:

    <http://cvmon-otb.rhcloud.com>

