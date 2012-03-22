monupco.com registration agent for OpenShift Express / Python
applications.

It compiles a list of locally installed Python packages and sends it to
monupco.com.


Installing on your OpenShift application
----------------------------------------

Create an account at <http://monupco.com>

Create a Python application on OpenShift

::

    rhc-create-app -a myapp -t python-2.6

Add a dependency in your setup.py file

::

    from setuptools import setup

    setup(
        name='MyApplication',
        version='1.0',
        install_requires=['monupco-openshift-express-python'],
     )

Set your userID in the ./data/MONUPCO_SETTINGS file

::

    cd ./myapp/
    echo "export MONUPCO_USER_ID=YourUserID"       >  ./data/MONUPCO_SETTINGS

OpenShift by default will treat your application as a package. If the name given in
setup.py is different from the name passed to rhc-create-app command then
set the application name in the ./data/MONUPCO_SETTINGS file

::

    echo "export MONUPCO_APP_NAME='MyApplication'" >> ./data/MONUPCO_SETTINGS

This registration script will ignore package names that match the value of 
OPENSHIFT_GEAR_NAME and MONUPCO_APP_NAME environment variables.


Enable the registration script in .openshift/action_hooks/post_deploy

::

    # Activate VirtualEnv in order to use the correct libraries
    source $OPENSHIFT_GEAR_DIR/virtenv/bin/activate

    # Set user defined settings
    source $OPENSHIFT_REPO_DIR/data/MONUPCO_SETTINGS

    # Register/update the application
    python $OPENSHIFT_GEAR_DIR/virtenv/bin/monupco-openshift-express-python

Then push your application to OpenShift

::

    git push

That's it, you can now check your application statistics at
<http://monupco.com>
