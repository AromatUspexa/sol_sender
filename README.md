# SOL sender 
[ [Channel](https://t.me/temporarily_crypto) ]


## Запуск под Windows
- Установите [Python 3.11](https://www.python.org/downloads/windows/). Не забудьте поставить галочку напротив "Add Python to PATH".
- Установите пакетный менеджер [Poetry](https://python-poetry.org/docs/): [инструкция](https://teletype.in/@alenkimov/poetry).
- [Скачайте](https://github.com/AromatUspexa/sol_sender/archive/refs/heads/main.zip) папку проекта и разархивируйте в удобном месте.
- Запустите `install.bat` для установки необходимых библиотек
- Зпустите `start.bat` для запуска скрипта

## Работа со скриптом

В файл `from_wallets.txt` вставьте private key своих SOL кошельков, с которых будут отправляться деньги. 
В файл `to_address.txt` вставьте адресса SOL кошельков, куда будут отправляться SOL 

Каждому приватному ключу соответствует свой адресс SOL!
**private_key -> wallet**
```
private_key1 --> wallet1
private_key2 --> wallet2
...
```
