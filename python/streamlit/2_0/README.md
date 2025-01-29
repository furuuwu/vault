# 2 - Uploading, Downloading, and Manipulating Data

Palmer's penguins

* dataset about Arctic penguins that comes from the work of Dr. Kristen Gorman (<https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php>) and the Palmer Station, Antarctica LTER (<https://pallter.marine.rutgers.edu/>)

## visualization

see

* `penguins.py`: uses matplotlib
* `penguins_altair.py`: uses altair

## file upload

To upload files, use `file_uploader()`. The default user-uploaded file has a value of None. There are two common scenarios

* `file_upload_v1.py`: provide a default file to use until the user uploads their file
* `file_upload_v2.py`: stop the app until a file is uploaded (using `stop()`)

## caching and state management

* `caching.py`
* `buttons.py`
* `session_presistence.py`
