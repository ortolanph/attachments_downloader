if __name__ == '__main__':
    pass

# 1. Create target.folder directory if it does not exist
# 2. Get batch.size messages where:
#   2.1. processed
#   2.2. no downloaded
# 3. For each message
#   3.1. Create target.folder.messageId directory
#   3.2. Fetch label data
#   3.3. Fetch download data
#   3.4. Generate index.html from template
#   3.5. Generate files from download data
#   3.6. Update database with downloaded flag
# 4. Create or update index with processed and downloaded messages of target.folder destination
