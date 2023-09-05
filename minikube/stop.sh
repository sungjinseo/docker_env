minikube stop

# Remove it from .bashrc
sed -i "/^alias k=/d" ~/.bashrc
sed -i "/^complete -o default -F __start_kubectl/d" ~/.bashrc
source ~/.bashrc
