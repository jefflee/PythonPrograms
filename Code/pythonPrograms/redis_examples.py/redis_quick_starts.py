import redis

# Refer to
# https://redis.io/docs/latest/develop/connect/clients/python/

print("======================  Connect  =========================")
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

print("======================  A simple string  =========================")
r.set('mytest:foo', 'bar')
val = r.get('mytest:foo')
print(val)

print("======================  Store and retrieve a dict.  =========================")
r.hset('mytest:user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

val = r.hgetall('mytest:user-session:123')
emptyResult = r.hgetall('mytest:user-session:99999')
print(val)
print(emptyResult)
