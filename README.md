# challenge_eurekalabs
To test locally run:
```bash
docker-compose up -d
```

Available endpoints:

Sign-up
```bash
curl --location 'http://localhost:8000/auth/accounts/sign-up' \
--form 'email="test@mail.com"' \
--form 'name="test"' \
--form 'password="1234"' \
--form 'password2="1234"' \
--form 'last_name="test"'
```

Log in
```bash
curl --location 'http://localhost:8000/auth/accounts/login'
--form 'email="test@mail.com"' \
--form 'password="1234"'
```

Get market data:
```bash
curl --location 'http://localhost:8000/market/?symbol=meta' \
--header 'Authorization: Bearer {acces_token}' \
```
obtain token using the log in endpoint
valid query params are: "META", "AAPL", "MSFT", "GOOGL", "AMZN" (lowercase is allowed) 

next step would be to implement a logger middleware 
for example : https://pypi.org/project/django-logging-middleware/

next implement Throttling
using drf default Throttling: rest_framework.throttling

both are pretty straightforward but i did not had enough time to implement them

as for the deploy, since the app is dockerized should be pretty simple to deploy it using Amazon Elastic Container Service