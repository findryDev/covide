from requestData import requestPlotsData
import plots
import htmlLinux

if __name__ == "__main__":
    plots.create_plot(requestPlotsData())
    htmlLinux.htmlMaker()
