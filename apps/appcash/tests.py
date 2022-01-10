from django.test import TestCase

# Create your tests here.



ALTER ROLE khalane SET client_encoding TO 'utf8';
ALTER ROLE khalane SET default_transaction_isolation TO 'read committed';
ALTER ROLE khalane SET timezone TO 'UTC';


GRANT ALL PRIVILEGES ON DATABASE myproject TO khalane;

python3 -m venv bizenv


source bizenv/bin/activate
