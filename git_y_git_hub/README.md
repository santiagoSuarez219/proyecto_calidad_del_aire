# Configuracion de SSH

1. Generar una llave SSH en la maquina local

```bash
ssh-keygen -t rsa -b 4096 -C "
```

2. Iniciar el ssh-agent en background

```bash
eval "$(ssh-agent -s)"
```

3. Agregar la llave SSH al ssh-agent

```bash
ssh-add ~/.ssh/id_rsa
```


