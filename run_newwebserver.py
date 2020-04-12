#!/usr/bin/env python3

import boto3
import sys
import time
import subprocess
import datetime


#Varaibles
string1 = 'Name'
string2 = 'My web Server'  
fileTxt = open('textFile.txt', 'w+')
readFileTxt = open('textFile.txt', 'r')
userText = """#!/bin/bash
                yum update -y
                yum install httpd -y
                systemctl enable httpd
                systemctl start httpd"""
ec2 = boto3.resource('ec2')
s3 = boto3.resource("s3")
object_name = 'image.jpg'
key = 'witacsresources'

#Menu layout
def print_menu():

    print('+-----------------------------------------------------------+')
    print('|                                                           |')
    print('|                           AWS                             |')
    print('|                                                           |')
    print('+-----------------------------------------------------------+')
    print('|   -1-   | Run Program                                     |')
    print('+-----------------------------------------------------------+')
    print('|   -2-   | List Instance                                   |')
    print('|   -3-   | Terminate Instance                              |')
    print('+-----------------------------------------------------------+')
    print('|   -4-   | List Buckets                                    |')
    print('|   -5-   | Terminate Bucket                                |')
    print('+-----------------------------------------------------------+')
    print('|   -6-   | View Log File                                   |')
    print('|   -7-   | Cloud Watch Monitoring                          |')
    print('+-----------------------------------------------------------+')
    print('|   -8-   | Exit                                            |')
    print('+-----------------------------------------------------------+')    
    print("=====>> "); 

#runs menu for user to selection option
def run_menu():

    #prints user menu
    print_menu()


    option_loop=True  

    while option_loop:  

        option = input('Enter your choice [1-8]:   ')
        option = int(option)

        if option == 1:
           run_script()

        elif option == 2:
           list_instances()

        elif option == 3:
           terminate_instance()

        elif option == 4:
           list_buckets()

        elif option == 5:
           delete_bucket()

        elif option == 6:
           view_log_file()

        elif option == 7:
           cloud_watch_data()

        elif option == 8:
            exit()

        else:
            print("Incorrect option, Enter any key to try again..")
     
#runs assignment script
def run_script():

    bucket_name = input( 'Please enter a bucket name: ')

    #download image from bucket
    s3.Bucket(key).download_file(object_name,'image.jpg')
    
    #create bucket
    try:
        print('.............Creating Bucket..............')
        bucket = s3.create_bucket(Bucket = bucket_name, ACL ='public-read', CreateBucketConfiguration = {'LocationConstraint': 'eu-west-1'})
        print ('Bucket Name : ' + bucket_name)
        fileTxt.write('\n Bucket created, Name : ' + bucket_name)
    except Exception as error:
        print (error)


    #put image into bucket
    try:
        print('.............Putting Image Into Bucket..............')
        response = s3.Object(bucket_name, object_name).put(Body = open(object_name, 'rb'))
        object = s3.Bucket(bucket_name).Object(object_name)
        object.Acl().put(ACL='public-read')
        print ('Bucket Image uploaded')
    except Exception as error:
        fileTxt.write('\n Error when creating bucket')
        print (error)

    #sg-06ed518f0b82030e0
    #Creating Instance
    print('...........Creating Instance........')
    security_group = input('Please enter your security group id :  ')
    #ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-099a8245f5daa82bf', # specifies the AMI ID of the instance we want to create
        MinCount=1, # min number of instances to launch
        MaxCount=1, # max number of instaces to launch
        KeyName='mbarcoeweb_keypair', # created in aws portal, key pair for access to the instance
        UserData= userText,
        InstanceType='t2.micro', # specifies what type/size of hardware needed
        SecurityGroupIds=[security_group],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': string1,
                        'Value': string2
                    },
                ]
            },
        ]
        )


    #id Of instance
    instance_id = instance[0].id

    print('----------------Instance Created----------------')
    fileTxt.write('Instance Created')


    print ('Instance Id : ' + instance_id)
    fileTxt.write('\n Instance Id : ' + instance_id)

    time.sleep(30)

    print('----------------Fetching Ip------------------')
    instance[0].wait_until_running()
    instance[0].load()

    instance_ip = instance[0].public_ip_address
    print('Instance Ip: ' + instance_ip)
    fileTxt.write('\n Instance Public Ip : ' + instance_ip)

    print('Loading Instance.........')
    time.sleep(20)

    #instance_ip = '54.171.235.200'

    ssh_cmd = 'ssh -o StrictHostKeyChecking=no -i mbarcoeweb_keypair.pem ec2-user@' + instance_ip

    print('----------------Creating Html file----------------')
    fileTxt.write('\n Creating Html file ')

    #creates html tag and file
    x1 = 'echo "<html>" > index.html'
    subprocess.run(x1, shell = True)
    print('Created text file and added html tag')
    fileTxt.write('\n Created text file and added html tag')

    #Writes a header text page to html file
    x2 = 'echo "<h2> Test page </h2>" >> index.html'
    subprocess.run(x2, shell = True)
    print('Added header to html file')
    fileTxt.write('\n Added header to html file')

    time.sleep(10)

    #Prints Instance Ip to html file
    x3 = 'echo "<br>Instance ID:   " >> index.html'
    subprocess.run(x3, shell = True)
    cmd1 = ssh_cmd + " curl --silent http://169.254.169.254/latest/meta-data/instance-id/ >> index.html"
    subprocess.run(cmd1, shell = True)
    print('Instance id loaded to html page')
    fileTxt.write('\n Instance id loaded to html page')


    #Prints availability zone to html file
    x4 = 'echo "<br>Availability zone:  " >> index.html'
    subprocess.run(x4, shell= True)
    cmd2 = ssh_cmd + " curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/ >> index.html"
    subprocess.run(cmd2, shell= True)
    print('Availability-zone loaded to html page')
    fileTxt.write('\n Availability-zone loaded to html page')


    #Prints ip address to html file
    x5 = 'echo "<br>IP address : " >> index.html'
    subprocess.run(x5, shell= True)
    cmd3 = ssh_cmd + " curl --silent http://169.254.169.254/latest/meta-data/public-ipv4 >> index.html"
    subprocess.run(cmd3, shell =True)
    print('Ip address loaded to html page')
    fileTxt.write('\n Ip address loaded to html page')

    #Prints ip address to html file
    x55 = 'echo "<br> DNS : " >> index.html'
    subprocess.run(x55, shell= True)
    cmd3 = ssh_cmd + " curl --silent http://169.254.169.254/latest/meta-data/public-hostname >> index.html"
    subprocess.run(cmd3, shell =True)
    print('DNS loaded to html page')
    fileTxt.write('\n DNS loaded to html page')

     #Prints Instance Type to html file
    x555 = 'echo "<br>Type : " >> index.html'
    subprocess.run(x555, shell= True)
    cmd333 = ssh_cmd + " curl --silent http://169.254.169.254/latest/meta-data/instance-type >> index.html"
    subprocess.run(cmd333, shell =True)
    print('Instance Type loaded to html page')
    fileTxt.write('Instance Type loaded to html page')

    #Print image to 
    x6 = 'echo "<br>Here is the image: <br>" >> index.html'
    subprocess.run(x6, shell= True)
    cmd4 = 'echo "<img src = https://"' + bucket_name + '".s3-eu-west-1.amazonaws.com/image.jpg>" >> index.html'
    subprocess.run(cmd4, shell= True)
    print('Image Loaded')
    fileTxt.write('\n Image Loaded')

    print('Pushing Index File to Instance')
    fileTxt.write('\n Pushing Index File to Instance')
    time.sleep(10)

    #Copies local file index.html and push it to instance
    cmd5 = "scp -i mbarcoeweb_keypair.pem index.html ec2-user@" + instance_ip + "':.'"
    subprocess.run(cmd5, shell = True)
    print('Index.html pushed to instance')
    fileTxt.write('\n Index.html pushed to instance')

    time.sleep(40)

    # copies Index file and put it in /var/www/html/ directory
    cmd6 = ssh_cmd + " ' sudo cp index.html /var/www/html/index.html'"
    subprocess.run(cmd6, shell = True)
    print('File moved')
    fileTxt.write('\n File moved')
    fileTxt.close()
    print('Completed')

#Lists all instnaces and there states
def list_instances():

    print('------------Current Instances------------')
    for instance in ec2.instances.all():
        print ('Instance Id: ' + instance.id ,instance.state)

#terminates instance that is requested
def terminate_instance():

    term_inst = input('Are you sure you want to terminate instance? [y/n] ')

    if term_inst == 'y' :
        instance_id = input('Enter Instance id: ')
        instance = ec2.Instance(instance_id)
        response = instance.terminate()
        print ('Instance:' + instance_id + ' is terminated' )
    elif term_inst =='n':
        print('Termination Cancelled')
        run_menu()
    else: 
        print('error')
        terminate_instance()

#list all buckets
def list_buckets():

    for bucket in s3.buckets.all():
        print (bucket.name)

#terminates bucket if empty
def delete_bucket():

    t_bucket = input('Please Enter Bucket name: ')
    bucket = s3.Bucket(t_bucket)
    
    try:
        response = bucket.delete()
        print (response)
    except Exception as error:
        print (error)

#prints log file
def view_log_file():
   print(fileTxt.read())

def cloud_watch_data():

    cloudwatch = boto3.resource('cloudwatch')
 
    instid = input("Please enter instance ID: ")    # Prompt the user to enter an Instance ID
    time.sleep(1000)
    instance = ec2.Instance(instid)
    #instance = ec2.Instance(instance_id)
    instance.monitor()       # Enables detailed monitoring on instance (1-minute intervals)

    metric_iterator = cloudwatch.metrics.filter(Namespace='AWS/EC2',
                                                MetricName='CPUUtilization',
                                                Dimensions=[{'Name':'InstanceId', 'Value': instance_id}])

    metric = list(metric_iterator)[0]    # extract first (only) element

    response = metric.get_statistics(StartTime = datetime.utcnow() - timedelta(minutes=5),   # 5 minutes ago
                                     EndTime=datetime.utcnow(),                              # now
                                     Period=300,                                             # 5 min intervals
                                     Statistics=['Average'])

    print ("Average CPU utilisation:", response['Datapoints'][0]['Average'], response['Datapoints'][0]['Unit'])
    # print (response)   # for debugging only

    time.sleep()

run_menu()