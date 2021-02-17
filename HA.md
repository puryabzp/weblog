-with this setting we can to apply more than one policy to a single request


-for throttle based on request’s IP we can use django-ip-restriction that with this middleware we can restrict incoming IPs to a Django project.
for e.g ALLOWED_IPS = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
and then we can define in our apis tthoe ip's to can access to request to our api's and this middleware Makes it easy for us to limit based on IPs

