# URL2PIC - Documentation
## Setup
*You need to have Docker installed to use this API.* <br> <br>
First clone the repo :
```
git clone https://github.com/R4z1xx/url2pic.git
cd url2pic/url2pic_api/
```
Build the Docker image :
```
docker build -t url2pic .
```
And start a new container : 
```
docker run -d -p 5000:5000 --name url2pic_api url2pic
```


## Usage
You can interact with this API by both methods.
### With url2pic.py script
*Don't forget to modify API url in the url2pic.py file (line 6)*
```
python url2pic.py http://example.com
```

### With curl and jq on Linux 
*Make sure to replace the "localhost" url by your API IP or domain.*
```
curl -s -X POST -H "Content-Type: application/json" -d "{\"url\": \"http://example.com\"}" http://localhost:5000/capture | jq -r .screenshot | base64 -d > screenshot.png
```
