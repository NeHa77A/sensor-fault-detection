import sys

def err_message_detail(err, err_details):
    _,_ , exc_tb = err_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    err_message = "Error Occurred in python Script [{0}] line Number [{1}] Error message [{2}]".format(file_name, exc_tb.tb_lineno, str(err))
    return err_message

class SensorException(Exception):
    def __init__(self, err_message, err_details):
        super().__init__(err_message)
        self.err_message = err_message_detail(
            err_message, err_details =err_details
        )

    def __str__(self) -> str:
        return self.err_message