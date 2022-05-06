## Boot Up Using Compose
docker-compose up -d
docker-compose logs -f worker

## Send Work Manually
```
Run redis-cli 
LPUSH queue:factoring '{"name": "meow"}'
LPUSH queue:factoring '{"name": "meowkkaggagaga"}'
```
## Try Scaling

Run docker-compose scale worker=2

and try putting in more work
