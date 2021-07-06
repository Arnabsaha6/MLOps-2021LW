#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()

cmd = f.getvalue("x")

#--------------------------------------particular---namespace------------------------------------------------------------------
if "in" in cmd: #for namespace filter
    command,namespace = cmd.split("in")

    if "get" in command or "show" in command: #show resources in a namespace
        #eg-> show pods in <ns>
        if "pod" in command or "pods" in command:
            print(subprocess.getoutput(f"kubectl get pods -n {namespace} --kubeconfig admin.conf"))

        elif "svc" in command or "services" in command or "service" in command:
            print(subprocess.getoutput(f"kubectl get svc -n {namespace} --kubeconfig admin.conf"))

        elif "deployment" in command or 'deploy' in command or 'deployments' in command or ' deploys' in command:
            print(subprocess.getoutput(f"kubectl get deployments -n {namespace} --kubeconfig admin.conf"))

#---------------------------------------------------delete------------------------------------------------------
    elif "delete" in command or 'del' in command or 'remove' in command: #delete resources in a namespace
        #eg-> delete/remove all pods in <ns> or delete pod <name> in <ns>
        if 'pod' in command or 'pods' in cmd: #delete pods in a namespace
            if 'all' in command:
                print(subprocess.getoutput(f'kubectl delete --all pods -n {namespace} --kubeconfig admin.conf'))
            else:
                operation , pod_name = command.split('pod')
                print(subprocess.getoutput(f'kubectl delete po {pod_name} -n {namespace} --kubeconfig admin.conf'))
        

        elif 'service' in command or 'services' in command: #delete sevices in a namespace
            if 'all' in command:
                print(subprocess.getoutput(f'kubectl delete --all svc -n {namespace} --kubeconfig admin.conf'))
            else:
                operation , svc_name = command.split('service')
                print(subprocess.getoutput(f'kubectl delete svc {svc_name} -n {namespace} --kubeconfig admin.conf'))


        elif 'deployment' in command or 'deployments' in command or 'deploy' in command: #delete deployments  in a namespace
            if 'all' in command:
                print(subprocess.getoutput(f'kubectl delete --all deploy -n {namespace} --kubeconfig admin.conf'))
            else:
                operation , deploy_name = command.split('deployment')
                print(subprocess.getoutput(f'kubectl delete deploy {deploy_name} -n {namespace} --kubeconfig admin.conf'))

        elif 'everything' in command or 'all' in command: #delete everything in the ns
            print(subprocess.getoutput('kubectl delete all --all -n {namespace} --kubeconfig admin.conf'))
#------------------------------------------------create----------------------------------------------------------------

    elif 'create' in command or 'run' in command or 'launch' in command: #launch resources in a namespace
        #eg-> launch pod <pod-name> with <img-name> in <namespace>
        if 'pod'  in command and 'with' in command: #launch a pod  in a namespace
            operation,pod_img = command.split('pod')
            pod_name,img = pod_img.split('with')
            print(subprocess.getoutput(f'kubectl run {pod_name} --image {img} -n {namespace} --kubeconfig admin.conf'))
        

        elif 'deployment' in command and 'with' in command: #launch deployments  in a namespace
            operation,deploy_img = command.split('deployment')
            deploy_name,img = deploy_img.split('with')
            print(subprocess.getoutput(f'kubectl create deployment  {deploy_name} --image {img} -n {namespace} --kubeconfig admin.conf'))

#--------------------------------------------------describe------------------------------------------------------

    elif 'describe' in command: #eg-> describe pods in <namespace>

        if 'pods' in command or 'pod' in command :
            print(subprocess.getoutput(f"kubectl describe pods -n {namespace} --kubeconfig admin.conf"))

        elif 'service' in command or 'services' in command or 'svc' in command:
            print(subprocess.getoutput(f"kubectl describe svc -n {namespace} --kubeconfig admin.conf"))

        elif 'deployment' in command or 'deploy' in command or 'deployments' in command:
            print(subprocess.getoutput(f"kubectl describe deploy -n {namespace} --kubeconfig admin.conf"))

#----------------------------------------------expose-----------------------------------------------------

    elif 'expose' in command: #eg-> expose pod <name> on <port no>
        if 'pod' in command:
            operation,detail = command.split("pod")
            pod_name,port = detail.split('on')
            port = int(port)
            print(subprocess.getoutput(f'kubectl expose pod {pod_name} -n {namespace} --port={port} --target-port=80  --type=NodePort --kubeconfig admin.conf '))
        
        elif 'deployment' in command:
            operation,detail = command.split("deployment")
            deploy_name,port = detail.split('on')
            print(subprocess.getoutput(f'kubectl expose deployment {deploy_name} -n {namespace} --port={port} --target-port --type=NodePort --kubeconfig admin.conf '))

#-------------------------------------scaling-------------------------------------------------------------------

    elif 'scale' in command: #scale deployment <name> by <no>
        if 'deployment' in command:
            operation,detail = command.split('deployment')
            deploy_name,no = detail.split('by')
            no=int(no)
            print(subprocess.getoutput(f'kubectl scale deployment {deploy_name} -n {namespace} --replicas={no} --kubeconfig admin.conf '))

        
#=======================================default namespace ========================================================================

elif "get" in cmd or "show" in cmd: #see resources in  default namespace
    #eg -> show pods 

    if "pod" in cmd or "pods" in cmd :
        print(subprocess.getoutput("kubectl get po --kubeconfig admin.conf"))

    elif "svc" in cmd or "services" in cmd or "service" in cmd:
        print(subprocess.getoutput("kubectl get svc --kubeconfig admin.conf"))

    elif "namespace" in cmd or 'namespaces' in cmd or 'ns' in cmd:
        print(subprocess.getoutput("kubectl get ns --kubeconfig admin.conf"))
    
    elif "deployment" in cmd or 'deploy' in cmd or 'deployments' in cmd or ' deploys' in cmd:
        print(subprocess.getoutput("kubectl get deployments --kubeconfig admin.conf"))


#--------------------------------------------remove----------------------------------------------------
elif 'remove' in cmd or 'delete' in cmd or 'del' in cmd: #delete resources in default namespace
    #eg-> remove pod <name> or remove all pods
    if 'pod' in cmd or 'pods' in cmd: #delete pods in default  namespace
        if 'all' in cmd:
            print(subprocess.getoutput('kubectl delete --all pods  --kubeconfig admin.conf'))
        else:
            operation , pod_name = cmd.split('pod')
            print(subprocess.getoutput(f'kubectl delete po {pod_name}  --kubeconfig admin.conf'))
        

    elif 'service' in cmd or 'services' in cmd: #delete sevices in default namespac
        if 'all' in cmd:
            print(subprocess.getoutput('kubectl delete --all svc --kubeconfig admin.conf'))
        else:
            operation , svc_name = cmd.split('service')
            print(subprocess.getoutput(f'kubectl delete svc {svc_name} --kubeconfig admin.conf'))


    elif 'deployment' in cmd or 'deployments' in cmd or 'deploy' in cmd: #delete deployments  in default namespace
        if 'all' in cmd:
            print(subprocess.getoutput('kubectl delete --all deploy --kubeconfig admin.conf'))
        else:
            operation , deploy_name = cmd.split('deployment')
            print(subprocess.getoutput(f'kubectl delete deploy {deploy_name}  --kubeconfig admin.conf'))

    elif 'namespace' in cmd or 'namespaces' in cmd or 'ns' in cmd: #delete namespaces
        if 'all' in cmd:
            print(subprocess.getoutput('kubectl delete --all namespace --kubeconfig admin.conf'))
        else:
            operation,ns_name = cmd.split('namespace')
            print(subprocess.getoutput(f'kubectl delete namespace {ns_name} --kubeconfig admin.conf'))
    
    elif 'everything' in cmd or 'all' in cmd:
            print(subprocess.getoutput('kubectl delete all --all  --kubeconfig admin.conf'))

#-------------------------------------------create-----------------------------------------------
elif 'create' in cmd or 'run' in cmd or 'launch' in cmd: #launch resources in a namespace
        #eg-> launch pod <pod-name> with <img-name> 
    
    if 'pod'  in cmd and 'with' in cmd: #launch a pod  in a namespace
        operation,pod_img = cmd.split('pod')
        pod_name,img = pod_img.split('with')
        print(subprocess.getoutput(f'kubectl run {pod_name} --image {img}  --kubeconfig admin.conf'))
    
    elif 'deployment' in cmd and 'with' in cmd: #launch deployments  in a namespace
        operation,deploy_img = cmd.split('deployment')
        deploy_name,img = deploy_img.split('with')
        print(subprocess.getoutput(f'kubectl create  deployment {deploy_name} --image {img} --kubeconfig admin.conf'))

    elif 'namespace' in cmd :
        op,ns = cmd.split('namespace')
        print(subprocess.getoutput(f'kubectl create namespace {ns} --kubeconfig admin.conf'))


#---------------------------------------describe-----------------------------------------
elif "describe" in cmd: #eg- describe pods
    if 'pods' in cmd or 'pod' in cmd :
        print(subprocess.getoutput("kubectl describe pods --kubeconfig admin.conf"))

    if 'service' in cmd or 'services' in cmd or 'svc' in cmd:
        print(subprocess.getoutput("kubectl describe svc --kubeconfig admin.conf"))

    if 'deployment' in cmd or 'deploy' in cmd or 'deployments' in cmd:
        print(subprocess.getoutput("kubectl describe deploy --kubeconfig admin.conf"))

#----------------------------------------expose - in -default---------------------------------------------

elif 'expose' in cmd: #eg-> expose pod <name> on <port no>
    if 'pod' in cmd:
        operation,detail = cmd.split("pod")
        pod_name,port = detail.split('on')
        print(subprocess.getoutput(f'kubectl expose pod {pod_name} --port={port} --target-port=80 --type=NodePort  --kubeconfig admin.conf'))
        
    elif 'deployment' in cmd:
        operation,detail = cmd.split("deployment")
        deploy_name,port = detail.split('on')
        print(subprocess.getoutput(f'kubectl expose deployment {deploy_name} --port={port} --target-port=80 --type=NodePort  --kubeconfig admin.conf'))

#-------------------------------------scaling-------------------------------------------------------------------

elif 'scale' in cmd: #scale deployment <name> by <no>
    if 'deployment' in cmd:
        operation,detail = cmd.split('deployment')
        deploy_name,no = detail.split('by')
        print(subprocess.getoutput(f'kubectl scale deployment {deploy_name}  --replicas={no} --kubeconfig admin.conf'))

elif 'cluster' in cmd and 'about' in cmd:
    print(subprocess.getoutput('kubectl cluster-info --kubeconfig admin.conf'))

elif 'clear' in cmd:
    print()
else:
    print(subprocess.getoutput(cmd+" --kubeconfig admin.conf"))