import os, sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='name of docker container', default="training-job-template")
parser.add_argument('--version', help='version tag of docker container', default="latest")
parser.add_argument('--proxy', help="proxy server to use (for both http and https)", default=None)
parser.add_argument('--image_prefix', help='image prefix to use', default="")
parser.add_argument('--deploy', help='deploy docker container to remote', action='store_true')

args, unknown = parser.parse_known_args()
if unknown:
    print("Unknown arguments "+str(unknown))

# Wrapper to print out command
def call(command):
    print("Executing: "+command)
    return subprocess.call(command, shell=True)

service_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
if args.name:
    service_name = args.name

# docker build
if args.proxy:
    proxy_args = "--build-arg http_proxy={} " \
                 "--build-arg https_proxy={} " \
                 "--build-arg no_proxy=localhost,127.0.0.1".format(args.proxy, 
                                                                   args.proxy)
else:
    proxy_args = ""

versioned_image = service_name+":"+str(args.version)
latest_image = service_name+":latest"
failed = call("docker build -t "+versioned_image+" -t "+latest_image+" "+proxy_args+" ./")

if failed:
    print("Failed to build container")
    sys.exit()

REMOTE_IMAGE_PREFIX = args.image_prefix

remote_versioned_image = REMOTE_IMAGE_PREFIX + versioned_image
call("docker tag " + versioned_image + " " + remote_versioned_image)

remote_latest_image = REMOTE_IMAGE_PREFIX + latest_image
call("docker tag " + latest_image + " " + remote_latest_image)

if args.deploy:
    call("docker push " + remote_versioned_image)

    if "SNAPSHOT" not in args.version:
    # do not push SNAPSHOT builds as latest version
        call("docker push " + remote_latest_image)
