Installation
============

Preparing Server
----------------

Assuming a freshly provisioned and updated server. I might try to rework this
to use Salt in the future. In any case, it seems as though I will use Fabric
to assist in bootstrapping the newly provisioned server as it will eliminate
much typing. I like automation.


Install Database
''''''''''''''''

Install Postgres on Ubuntu

.. code-block:: bash

	$ sudo apt-get install postgresql
	$ sudo apt-get install libpq-dev python-dev
	$ sudo -u postgres psql postgres
	postgres=# \password postgres
	postgres=# \q

Create database user and database

.. code-block:: bash

	$ sudo su postgres
	$ createuser --interactive
	$ createdb -O whatever-username-you-used database-name

Install Nginx
'''''''''''''

.. code-block:: bash

 	$ sudo apt-get install nginx


Install Utilities
'''''''''''''''''

.. code-block:: bash

 	$ sudo apt-get install git
 	$ sudo apt-get install virtualenvwrapper





Contents:

.. toctree::
   :maxdepth: 2

   install