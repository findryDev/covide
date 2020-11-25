from cov.requestData import requestPlotsData
from cov.httpd import restart
import cov.timeControl
import cov.plots
import cov.htmlLinux
import os
import logging
from logging.handlers import SMTPHandler
from time import sleep
from dotenv import load_dotenv
load_dotenv()

# create a custom logger
loggerCounter = logging.getLogger('counter')
loggerCounter.setLevel(logging.DEBUG)
loggerMain = logging.getLogger(__name__)
loggerMain.setLevel(logging.DEBUG)
loggerEmail = logging.getLogger('email')
loggerEmail.setLevel(logging.INFO)

# create handlers
print_handler = logging.StreamHandler()
file_handler = logging.FileHandler('mainFile.log')
mailhost = (os.getenv('host'), os.getenv('port'))
fromaddr = os.getenv('fromaddr')
toaddrs = os.getenv('toaddrs')
subject = 'Email Logger'
credentials = (os.getenv('use'), os.getenv('password'))
email_handler = SMTPHandler(mailhost=mailhost,
                            fromaddr=fromaddr,
                            toaddrs=[toaddrs],
                            subject=subject,
                            credentials=credentials,
                            secure=())
# create formatters and add it to handlers
print_format = logging.Formatter('%(asctime)s - %(message)s')
print_handler.setFormatter(print_format)
file_format = logging.Formatter('%(levelname)s - %(asctime)s \
- %(message)s\
- %(name)s')
file_handler.setFormatter(file_format)
email_format = logging.Formatter("""%(asctime)s \
                                 - %(levelname)s \
                                 - %(message)s \
                                 - %(name)s \
                                 - %(filename)s \
                                 - %(process)d""")
email_handler.setFormatter(email_format)
# add handler to the logger
loggerMain.addHandler(print_handler)
loggerMain.addHandler(file_handler)
loggerCounter.addHandler(print_handler)
loggerEmail.addHandler(email_handler)


while True:
    try:
        if __name__ == "__main__":
            loggerMain.debug('Start script')
            loggerEmail.info('Start script')
            cov.plots.create_plot(requestPlotsData())
            loggerMain.debug('Finished create plots')
            cov.htmlLinux.htmlMaker()
            loggerMain.debug('Created html')
            restart()
            loggerMain.debug('Apache restart')
            loggerMain.debug('End scripts')
            loggerEmail.info('End scripts')
            waitSeconds = cov.timeControl.waitTo(8)
            for i in range(waitSeconds, 0, -1):
                loggerCounter.info(f'Wait {i}')
                sleep(1)
    except Exception as e:
        loggerMain.error("Exception occurred", exc_info=True)
        loggerEmail.error(f"Exception occurred: {e}", exc_info=True)
        break
