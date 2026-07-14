from dnacentersdk import DNACenterAPI

dnac = DNACenterAPI(
    base_url="https://sandboxdnac.cisco.com",
    username="devnetuser",
    password="Cisco123!",
    version="2.3.5.3",     # match your Catalyst Center version
    verify=False           # sandbox uses a self-signed cert
)

images = dnac.software_image_management_swim.get_software_image_details()

for img in images.response:
    print(img.name, img.version, img.imageUuid, img.isGoldenTagged)

dnac.software_image_management_swim.tag_as_golden_image(
    imageId="<image-uuid>",
    deviceFamilyIdentifier="<family-id>",
    deviceRole="ALL",          # ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, ALL, UNKNOWN
    siteId="-1"                # -1 = global
)

distribution = dnac.software_image_management_swim.trigger_software_image_distribution(
    payload=[{
        "deviceUuid": "<device-uuid>",
        "imageUuid": "<image-uuid>"
    }]
)

# distribution.response.taskId is returned immediately (async)
task_result = dnac.task.wait_for_task_complete(distribution, timeout=600)

if task_result.response.isError:
    raise Exception(task_result.response.failureReason)
print("Distribution complete")

activation = dnac.software_image_management_swim.trigger_software_image_activation(
    payload=[{
        "deviceUuid": "<device-uuid>",
        "imageUuidList": ["<image-uuid>"],
        "activateLowerImageVersion": False,
        "distributeIfNeeded": True
    }]
)

task_result = dnac.task.wait_for_task_complete(activation, timeout=1200)
print("Activation error?", task_result.response.isError)

def upgrade_device(dnac, device_uuid, image_uuid):
    # Stage (non-disruptive)
    dist = dnac.software_image_management_swim.trigger_software_image_distribution(
        payload=[{"deviceUuid": device_uuid, "imageUuid": image_uuid}]
    )
    if dnac.task.wait_for_task_complete(dist, timeout=600).response.isError:
        raise Exception("Distribution failed")

    # Activate (disruptive – reload)
    act = dnac.software_image_management_swim.trigger_software_image_activation(
        payload=[{"deviceUuid": device_uuid,
                  "imageUuidList": [image_uuid],
                  "distributeIfNeeded": True,
                  "activateLowerImageVersion": False}]
    )
    if dnac.task.wait_for_task_complete(act, timeout=1200).response.isError:
        raise Exception("Activation failed")

    return "Upgrade complete"