# Run_newWebServer App

As Part of a second year assignment we were tasked with creating a Python script that retrieves an image from a url , uploads it to a personal bucket.Launches an ec2 instance, installs apache web server, then displays the image from my personal bucket onto the web page and also some instance meta data.

## App Walkthrough

When the script has ran the following menu will appear, where you can enter which option you would like to perform

### MENU
    +-----------------------------------------------------------+
    |                                                           |
    |                           AWS                             |
    |                                                           |
    +-----------------------------------------------------------+
    |   -1-   | Run Program                                     |
    +-----------------------------------------------------------+
    |   -2-   | List Instance                                   |
    |   -3-   | Terminate Instance                              |
    +-----------------------------------------------------------+
    |   -4-   | List Buckets                                    |
    |   -5-   | Terminate Bucket                                |
    +-----------------------------------------------------------+
    |   -6-   | View Log File                                   |
    |   -7-   | Cloud Watch Monitoring                          |
    +-----------------------------------------------------------+
    |   -8-   | Exit                                            |
    +-----------------------------------------------------------+

## Menu Walkthrough

### Option 1

Option 1 runs through the code for the assignment as in the description. when seletected the script will retrieve an image from a url , upload  it to a personal bucket. Launche an ec2 instance, installs apache web server, then displays the image from my personal bucket onto the web page and also some instance meta data. When ran you will be asked to enter a bucket name, a security group ID. After each event the user will be update on what is happening. For Example "Instance is being Created". After the script has run, user will be told that the script has finished and can view web page at the given ip.


### Option 2 - List Instance
Option 2 will List all instance of the user


### Option 3 Terminate Instance
Option 3 will ask the user for the Id of the instance they wish to terminate, then terminate the instance that was mentioned


### Option 4 - List Buckets
Option 4 will list the buckets for the user


### Option 5 - Terminate Bucket
Option 5 will ask the user for the bucket id that they wich to terminate.


### Option 6 - View Log File
Option 6  prints the log file to the screen , detailing the process of running option 1 and the details of the instance and bucket


### Option 7 - Cloudwatch Monitoring
Option 7  asks user for Instance id of which the would like to enable monitoring, after a time will print out monitoring data such as cpu usage.(Not working correctly)


### Option 8 - Exit
Option 8 will stops the script from running


## Built With

* Python
* Boto3
* Visual Studio

## Contributing

* https://www.reddit.com/r/aws/comments/80ocde/using_boto3_to_get_instance_name_tag_private_ip/
* http://queirozf.com/entries/python-3-subprocess-examples
* https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/s3-example-download-file.html
* https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/

## Authors

* @Michael Barcoe - barcoe98@gmail.com - https://github.com/barcoe98

## Acknowledgments

* https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
* @rFrisby



 

