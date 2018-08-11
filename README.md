# appleMusicTokenGen
To use the Apple Music API, you must have a signed JWT in your request header

According to [Apple's docs](https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens),
> To make requests to the Apple Music API, [Create a MusicKit identifier and private key](https://help.apple.com/developer-account/#/devce5522674) using a developer token to authenticate yourself as a trusted developer and member of the Apple Developer Program. A signed developer token is required in the header of every Apple Music API request.

## What you'll need
- A machine with Python 2.7+ and root access
- A 10-character key identifier [configured for use with the MusicKit Service](https://help.apple.com/developer-account/#/dev646934554)
- A 10-character Apple Developer Program Team ID
- A MusicKit Private Key in a *.p8 file

### Required Python packages
For the Python script to execute, you'll need to have `pyjwt` and `cryptography` installed. You can get these packages with
```
sudo pip install pyjwt
```
and
```
sudo pip install cryptography
```

## Generating your JWT
### Step 1: Move your *.p8 private key to the current working directory
For example, if you are running the script from ~/Downloads/appleMusicTokenGen, then you should move the *.p8 file there.
### Step 2: Run the script and follow directions
```
python appleMusicTokenGen.py
```
The script will prompt you to enter your key identifier and Team ID.
### Step 3: Check the validity of your token
If all goes well, the script will output a curl command that you can run on your terminal. If your token is valid, the request will fetch some Maroon 5 albums! 

The response should look like:
```
{"data":[{"id":"1798556","type":"artists","href":"/v1/catalog/us/artists/1798556","attributes":{"name":"Maroon 5","genreNames":["Pop"],"url":"https://itunes.apple.com/us/artist/maroon-5/1798556"},"relationships":{"albums":{"data":[{"id":"1422002037","type":"albums","href":"/v1/catalog/us/albums/1422002037"},{"id":"1416228265","type":"albums","href":"/v1/catalog/us/albums/1416228265"},{"id":"1418286515","type":"albums","href":"/v1/catalog/us/albums/1418286515"},{"id":"1420695086","type":"albums","href":"/v1/catalog/us/albums/1420695086"},{"id":"1393182571","type":"albums","href":"/v1/catalog/us/albums/1393182571"},{"id":"1381588297","type":"albums","href":"/v1/catalog/us/albums/1381588297"},{"id":"1381582726","type":"albums","href":"/v1/catalog/us/albums/1381582726"},{"id":"1337482217","type":"albums","href":"/v1/catalog/us/albums/1337482217"},{"id":"1334625109","type":"albums","href":"/v1/catalog/us/albums/1334625109"},{"id":"1396162524","type":"albums","href":"/v1/catalog/us/albums/1396162524"},{"id":"1396133926","type":"albums","href":"/v1/catalog/us/albums/1396133926"},{"id":"1396139711","type":"albums","href":"/v1/catalog/us/albums/1396139711"},{"id":"1396141359","type":"albums","href":"/v1/catalog/us/albums/1396141359"},{"id":"1303939379","type":"albums","href":"/v1/catalog/us/albums/1303939379"},{"id":"1280722898","type":"albums","href":"/v1/catalog/us/albums/1280722898"},{"id":"1231170940","type":"albums","href":"/v1/catalog/us/albums/1231170940"},{"id":"1224301962","type":"albums","href":"/v1/catalog/us/albums/1224301962"},{"id":"1224306708","type":"albums","href":"/v1/catalog/us/albums/1224306708"},{"id":"1224306761","type":"albums","href":"/v1/catalog/us/albums/1224306761"},{"id":"1231170257","type":"albums","href":"/v1/catalog/us/albums/1231170257"},{"id":"1231171688","type":"albums","href":"/v1/catalog/us/albums/1231171688"},{"id":"1216552239","type":"albums","href":"/v1/catalog/us/albums/1216552239"},{"id":"1186926564","type":"albums","href":"/v1/catalog/us/albums/1186926564"},{"id":"1186926656","type":"albums","href":"/v1/catalog/us/albums/1186926656"},{"id":"1186926229","type":"albums","href":"/v1/catalog/us/albums/1186926229"}],"href":"/v1/catalog/us/artists/1798556/albums","next":"/v1/catalog/us/artists/1798556/albums?offset=46"}}}]}
```

## Copyright
© 2018 Pedro Sandoval
