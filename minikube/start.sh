sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube start --driver=docker

echo -e "\nalias k='kubectl'" >> ~/.bashrc
source ~/.bashrc

kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl
echo 'complete -o default -F __start_kubectl k' >> ~/.bashrc
source ~/.bashrc
