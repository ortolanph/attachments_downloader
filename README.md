# attachments_downloader

## Tasks:

### Step 1 - Acquire Ids

 - [x] Get all the messages to an empty database
 - [x] Check if ids are already on database and put only missing ids

### Step 2 - Fetch Data

 - [x] Select batch.size messages
 - [x] Get information of
   - [x] message
   - [x] labels
   - [x] attachment information
 - [x] Mark message as processed

### Step 3 - Download

 - [x] Create the target.folder
 - [x] Get batch.size messages where:
   - [x] processed
   - [x] not downloaded
 - [ ] For each message
   - [x] Create target.folder.messageId directory
   - [x] Fetch label data
   - [x] Fetch download data
   - [x] Generate index.html from template
   - [ ] Generate files from download data
   - [ ] Update database with downloaded flag
 - [ ] Create or update index with processed and downloaded messages of target.folder destination
