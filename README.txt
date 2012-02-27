This is a client side agent for monupco.com. It compiles
a list of locally installed Python packages and sends it to
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

Set your username and application name in the ./data/MONUPCO_SETTINGS file

::

    cd ./myapp/
    echo "export MONUPCO_USER_ID=YourUserID"       >  ./data/MONUPCO_SETTINGS

Enable the registration script in .openshift/action_hooks/post_deploy

::

    # Activate VirtualEnv in order to use the correct libraries
    source $OPENSHIFT_APP_DIR/virtenv/bin/activate

    # Set user defined settings
    source $OPENSHIFT_REPO_DIR/data/MONUPCO_SETTINGS

    # Register/update the application
    python $OPENSHIFT_APP_DIR/virtenv/bin/monupco-openshift-express-python

Then push your application to OpenShift

::

    git push

That's it, you can now checkout your application statistics at
<http://monupco.com>
