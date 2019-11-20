import constants.widget_constants as const
import tkinter as tk


class ScrollableListboxF(tk.Frame):
    """ Scrollable listbox."""

    def __init__(self,

                 parent):

        tk.Frame.__init__(self,
                          parent,
                          padx=const.SL_PADX,
                          pady=const.SL_PADY)

        self._lb_output = tk.Listbox(
            self,

            height=const.SL_OUTPUT_LISTBOX_HEIGHT,
            font=const.SL_FONT
        )

        self._x_scroll = tk.Scrollbar(
            self,

            orient=tk.HORIZONTAL,
            command=self._lb_output.xview
        )

        self._y_scroll = tk.Scrollbar(
            self,

            orient=tk.VERTICAL,
            command=self._lb_output.yview
        )

        self._lb_output.configure(xscrollcommand=self._x_scroll.set,
                                  yscrollcommand=self._y_scroll.set)

        self._x_scroll.pack(side='bottom',
                            fill='x')
        self._y_scroll.pack(side='right',
                            fill='y')

        self._lb_output.pack(side='left',
                             fill='both',
                             expand=True)

    #########################################################################
    # Public methods

    def add_new_session_output_entry(
            self,
            
            new_entry: str):
        """ 
        - Add information about a step in the training/testing session.

        :param new_entry: Information about a step in the training/testing
                          session.
        """

        self._lb_output.insert('end',
                               new_entry)

        self._lb_output.select_clear(last=self._lb_output.size(),
                                     first=0)

        self._lb_output.yview('end')

    def clear(self):
        """ Clears the listbox."""

        self._lb_output.delete(0, 'end')

    #########################################################################
