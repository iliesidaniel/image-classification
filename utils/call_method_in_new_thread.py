import threading


class CallMethodInNewThread:
    """ Calls a method in a new thread to speed up the execution."""

    @staticmethod
    def call_method(
            function_to_call,
            **kwargs):
        """ Creates a new thread that will call "function_to_call" passing
        "kwargs".

        :param function_to_call: Function that will be called.
        :param kwargs: Arguments of the called function.
        """

        t = threading.Thread(
            target=function_to_call,
            kwargs=kwargs,
            daemon=True
        )

        t.start()
