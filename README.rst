Difio registration agent for OpenShift / Python applications.

It compiles a list of locally installed Python packages and sends it to
<http://www.dif.io>.


Installing on your OpenShift application
----------------------------------------

Create an account at <http://www.dif.io>

Create a Python application on OpenShift

::

    rhc-create-app -a myapp -t python-2.6

Add a dependency in your setup.py file

::

    from setuptools import setup

    setup(
        name='MyApplication',
        version='1.0',
        install_requires=['difio-openshift-python'],
     )

Set your userID in the ./data/DIFIO_SETTINGS file

::

    cd ./myapp/
    echo "export DIFIO_USER_ID=YourUserID" > ./data/DIFIO_SETTINGS

OpenShift by default will treat your application as a package. If the name given in
setup.py is different from the name passed to rhc-create-app command then
set the application name in the ./data/DIFIO_SETTINGS file

::

    echo "export DIFIO_APP_NAME='MyApplication'" >> ./data/DIFIO_SETTINGS

This registration script will ignore package names that match the value of 
OPENSHIFT_GEAR_NAME and DIFIO_APP_NAME environment variables.


Enable the registration script in .openshift/action_hooks/post_deploy

::

    # Activate VirtualEnv in order to use the correct libraries
    source $OPENSHIFT_GEAR_DIR/virtenv/bin/activate

    # Set user defined settings
    source $OPENSHIFT_REPO_DIR/data/DIFIO_SETTINGS

    # Register/update the application
    python $OPENSHIFT_GEAR_DIR/virtenv/bin/difio-openshift-python

Then push your application to OpenShift

::

    git push

That's it, you can now check your application statistics at
<http://www.dif.io>
