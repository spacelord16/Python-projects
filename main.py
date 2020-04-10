# import COVID19Py
# import COVID19py as COVID19py
# import matplotlib.pyplot as plt
#
#
# covid19 = COVID19py.COVID19()
# data = covid19.getAll(timelines=True)
# virusdetails = dict(data["latest"])
# names = list(virusdetails.keys())
# values = list(virusdetails.values())
# plt.bar(range(len(virusdetails)), values, tick_label=names)
#
# plt.show()

from plyer import notification


def notifyMe(title, message):
    notification.notifyMe(
        title=title,
        message=message,
        app_icon=None,
        timeout=10
    )


if __name__ == '__main__':
    notifyMe("Aditya", "Lets stop the Virus from spreading together")
