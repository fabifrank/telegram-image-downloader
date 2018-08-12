# Telegram Image Downloader

Python script to sync images in a Telegram chat with a local folder (one-way download).

## How to

1. Register new api id and hash at [https://my.telegram.org](https://my.telegram.org)

2. Run the following command to build the docker container

```
docker build -t telegram-image-downloader .
```

3. Set Credentials in file `./credentials.env` (file is ignored via .gitignore)

```
TELEGRAM_API_ID=<API_ID>
TELEGRAM_API_HASH=<API_HASH>
TELEGRAM_PHONE=<PHONE_NUMBER>
TELEGRAM_DOWNLOAD_FOLDER=<DOWNLOAD_FOLDER_PATH>
TELEGRAM_CHATS=<CHAT_LIST> # comma separated list of chat names
```

4. Source the file

```
source credentials.env
```

5. Start downloading:

```
docker run -v $(pwd)/contents:/contents -it telegram-image-downloader /bin/bash -c "python /contents/download.py $TELEGRAM_API_ID $TELEGRAM_API_HASH $TELEGRAM_PHONE_NUMBER $TELEGRAM_DOWNLOAD_FOLDER \"$TELEGRAM_CHATS\""
```