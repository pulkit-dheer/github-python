import boto3


# def lambda_handler(event, context):



ec2 = boto3.client('ec2', region_name='ap-south-1')

response = ec2.describe_snapshots(OwnerIds=['self'])

instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['running']}])

active_instance_id = set()

for reservation in instances_response['Reservations']:
    for instance in reservation['Instances']:
        active_instance_id.add(instance['InstanceId'])

print(active_instance_id)


for snapshot in response['Snapshots']:
    snapshot_id = snapshot['SnapshotId']
    volume_id = snapshot.get("VolumeId")
    print(volume_id)
    print(snapshot_id)


    if not volume_id:
        print("I am here")
        # ec2.delete_snapshot(SnapshotId=snapshot_id)
        print(f"Deleted EBS snapshot {snapshot_id}")
    else:
        try:
            volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
            if not volume_response['Volumes'][0]['Attachments']:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted EBS snapshot {snapshot_id}")
        except ec2.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted EBS snapshot {snapshot_id}")