#!/bin/sh
#NeWare 2021 ~ Grup A
contrasenyaencriptada="$(mkpasswd --method=sha-512 $2)"
useradd -m -p $contrasenyaencriptada -s /bin/bash $1
usermod -g $3 $1
echo "S'ha Creat l'Usuari $1 amb Contrasenya $2 i amb Grup $3"
