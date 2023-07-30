# TestPushBot
This is the bot which start autotests and send information about run to ICQ

<h1> Upgrade lib mailru-im-bot </h1>
    <p> <h3 align="center">Для корректной работы бота по мониторингу с помощью шедулера необходимо видоизменить корневую библиотеку.</h3> 
    <h3>Для этого нужно:</h3> 
    <li> Открыть файл <code>bot.py</code>, принадлежащий библиотеке <code>mail-ru-bot</code>
    <li> Найти <code>def idle()</code> 
    <li> В цикле <code> while self.running:</code> внести строчку <code>schedule.run_pending()</code> 
