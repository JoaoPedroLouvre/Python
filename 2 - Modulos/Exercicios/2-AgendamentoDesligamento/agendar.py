import os

# Desliga após um minuto
os.system('shutdown')

# Desliga agora
os.system('shutdown now')

# Agendar desligamento após uma hora
os.system('shutdown 12:00')

# Agendar desligamento após meia hora
os.system('shutdown 11:30')

# Reinicia o computador após um minuto
os.system('shutdown -r')

# O mesmo sistema de agendamento de desligar funciona para reiniciar.