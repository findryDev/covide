from requestData import requestPlotsData
import plots
import htmlLinux
import logging

# create a custom logger
loggerMain = logging.getLogger(__name__)
loggerMain.setLevel(logging.DEBUG)
# create handlers
print_handler = logging.StreamHandler()
file_handler = logging.FileHandler('mainfile.log')
print_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)
# create formatters and add it to handlers
print_format = logging.Formatter('%(asctime)s - %(message)s')
print_handler.setFormatter(print_format)
file_format = logging.Formatter('%(levelname)s - %(asctime)s\
- %(message)s\
- %(name)s')
file_handler.setFormatter(file_format)
# add handler to the logger
loggerMain.addHandler(print_handler)
loggerMain.addHandler(file_handler)




if __name__ == "__main__":
    loggerMain.debug('Start script')
    plots.create_plot(requestPlotsData())
    loggerMain.debug('Finished create plots')
    htmlLinux.htmlMaker()
    loggerMain.debug('End scripts')
