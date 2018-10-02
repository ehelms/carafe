DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': "{{ database_name }}",
    'USER': "{{ database_user }}",
    'PASSWORD': "{{ database_password }}",
    'HOST': "{{ ansible_default_ipv4.address }}",
    'PORT': '5432',
    'CONN_MAX_AGE': 0
  },
}
# `SECRET_KEY`: A secret key for a particular Django installation. This is used to provide
# cryptographic signing, and should be set to a unique, unpredictable value.
# Pulp does not provide a default secret key. This must be user provided in order for the
# Pulp Django Application to run.
# SECURITY WARNING: keep the secret key used in production secret!
#
SECRET_KEY = "{{ secret_key }}"

# `DEBUG`: A boolean that turns on/off debug mode. See the Django docs for more information on the
# behaviors this affects.
#
DEBUG = True

# `MEDIA_ROOT`: Location where Pulp stores files (Artifacts, published metadata, etc)
#
# MEDIA_ROOT: /var/lib/pulp/

# Redis configuration
#
# `REDIS`: Redis provides the basis for the Pulp tasking system. For security ensure your Redis
# deployment can only be reached via trusted network endpoints per https://redis.io/topics/security.
# Pulp does support password based authenticated from the client. For encrypted communication
# of Redis traffic over untrusted networks Redis recommends spiped.
#
REDIS_HOST = "{{ ansible_default_ipv4.address }}"
REDIS_PORT =  6379
REDIS_PASSWORD = ''

# Server configuration
#
# `SERVER`: Server behavior configuration of pulp.
#   `WORKING_DIRECTORY`: Path for pulp workers to create temporary directories
#                        for completion of tasks
#
# SERVER:
#   WORKING_DIRECTORY: /var/lib/pulp/tmp

# Content Application
#
# `CONTENT`: The content serving application.
#   `WEB_SERVER`: The type of web server.  Must be: (django|apache|nginx).
#                 When set to 'apache', the X-SENDFILE header is injected which delegates
#                 streaming the content to Apache.  Requires: mod_xsendfile to be installed.
#                 When set to 'nginx', the X-Accel-Redirect header is injected which delegates
#                 streaming the content to NGINX.
#   `HOST`: The host name or IP and an optional port number for the Content App. (e.g.
#           example.com:8000) This value should be specified only if the Content App is served on
#           a host that's different from the REST API. The default value is the same as the host
#           used to serve the REST API.
#
# CONTENT:
#   WEB_SERVER: django
#   HOST: pulp.example.com
