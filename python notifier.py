from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("Notification",
                 "Remind me to shutdown my laptop ",
                 duration=2000)