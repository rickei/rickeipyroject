# sample AWS python sdk
# list out instances in ELB and show their state
# run by python3

# require aws access key in ~/.aws (make sure user has EC2 access, at least readonly)
# 
# require install boto3
# pip install boto3


## change : concat the tuple with '\n' to string and output , for nagios use

import boto3
	
client = boto3.client('elb')
ec2 = boto3.resource('ec2')
tup=()


elb = client.describe_load_balancers(
	LoadBalancerNames=[
        'your_ELB_Name'
    ]
 )
#print('--------')

#print(elb["LoadBalancerDescriptions"][0]["DNSName"]) 
tup=tup+(elb["LoadBalancerDescriptions"][0]["DNSName"],'\n','------------------','\n')

#print('--------')

instancehealth = client.describe_instance_health(
    LoadBalancerName='elb-estore',
    
)

for InstanceStates in instancehealth["InstanceStates"]:
    instance = ec2.Instance(InstanceStates["InstanceId"])
    #print(InstanceStates["InstanceId"], instance.tags[0].get('Value'),InstanceStates["State"], instance.private_ip_address, instance.public_ip_address, instance.state.get('Name'))
    tup = tup + (InstanceStates["InstanceId"],' ', instance.tags[0]["Value"],' ',InstanceStates["State"],' ', instance.private_ip_address, ' ',instance.public_ip_address,' ', instance.state["Name"],'\n') 


#print('--------')
s="".join(tup)

print(s)
