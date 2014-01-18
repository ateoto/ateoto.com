Installation
============

Preparing Server
----------------

Assuming a freshly provisioned and updated server.


Install Database
''''''''''''''''

Install Postgres on Ubuntu

 ::

	sudo apt-get install postgresql
	sudo -u postgres psql postgres
	\password postgres

Create database user and database

 ::

	sudo su postgres
	createuser --interactive
	createdb -U whatever-username-you-used

Install Nginx
'''''''''''''



Contents:

.. toctree::
   :maxdepth: 2

   install