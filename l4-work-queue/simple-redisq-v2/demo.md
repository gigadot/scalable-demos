http POST localhost:5000/factor number=100
http POST localhost:5000/factor number=1000
http POST localhost:5000/factor number=10000000
http POST localhost:5000/factor number=100000000

* Observe the nature of waiting

Replay the thing with docker-compose scale worker=2

