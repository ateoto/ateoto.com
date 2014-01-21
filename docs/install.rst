Installation
============

Preparing Server
----------------

Assuming a freshly provisioned and updated server.


Install Database
''''''''''''''''

Install Postgres on Ubuntu

.. code-block:: bash

	$ sudo apt-get install postgresql
	$ sudo -u postgres psql postgres
	postgres=# \password postgres
	postgres=# \q

Create database user and database

.. code-block:: bash

	$ sudo su postgres
	$ createuser --interactive
	$ createdb -U whatever-username-you-used

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