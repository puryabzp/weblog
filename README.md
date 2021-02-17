======================
about project:
======================
this is a weblog project based On Django Framework with sqlite db
also in this project use drf for made some RESTFUL api's





======================
Project sections
======================
this project has two application
1- Account:
In this program, items such as defining custom user modle, login, logout and registering the handle are discussed

2-blog:
In this section, items such as posts, comments and other items are handled...




=======================
about respina challenge
=======================
actually for this challenge used  drf rate limiter(Throttling) 
that you can see that in settings.py on 
https://github.com/puryabzp/weblog/blob/master/zoomit/zoomit/settings.py

actually with this setting i can use them to control the rate of requests that clients can make to an API.

'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle', ===> for anno users
        'rest_framework.throttling.UserRateThrottle' ===> for authenticated users(users that login)
    ],
	
	
	
	
	    'DEFAULT_THROTTLE_RATES': {  ====> in this section we can define different conditions for anno users and authenticated users
        'anon': '5/minute', ====> for e.g 5 request per minutes
        'user': '10/minute'
    }


***for this challenge i'd define an api that located in this directory with 'respina_view' name	
https://github.com/puryabzp/weblog/blob/master/zoomit/blog/api.py

with this config we cand handle rate limiting of requests on second, minute, hour or day
And if the number of requests exceeds the allowable limit, the user will be limited (according to the defined conditions)

***
For a better explanation,I have put pictures of the steps in a directory called respina_challenge
