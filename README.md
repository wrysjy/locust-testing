# load testing with locust
```python
docker-compose up --scale worker=4
```

#### master web server is running on port 8089
```
http://localhost:8089/
```
#### manual testing 
``` 
locust --host=http://127.0.0.1:8000 -f <your-locust-file.py>
```