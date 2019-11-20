import constants.global_constants as const

import tkinter as tk


class ScrollableCanvasC(tk.Canvas):
    """
    - Canvas with scrollbars.
    - The scrollbars pack themselves.
    - DO NOT use pack/grid/place for f_main_frame or it will nto scroll.
    - Place widgets inside f_main_frame, not directly inside the canvas.
    """

    def __init__(self,

                 parent,

                 canvas_anchor='nw',

                 horizontal_scroll=False,

                 **options):
        """
        All options from tk.Canvas are available.
        
        :param parent: Parent. 
        :param options: Options.
        """

        tk.Canvas.__init__(self,
                           parent,
                           options)

        self._horizontal_scroll = horizontal_scroll
        self._canvas_anchor = canvas_anchor
        self._parent = parent

        self._create_widgets()
        self._place_widgets()

    #########################################################################
    # Widget creation and placement.

    def _create_widgets(self):
        self.f_main_frame = tk.Frame(
            self,

            padx=const.FRAME_PADX,
            pady=const.FRAME_PADY
        )

        self.sb_v_scrollbar = tk.Scrollbar(
            self._parent,

            orient=tk.VERTICAL,
            command=self.yview
        )

        self.sb_h_scrollbar = tk.Scrollbar(
            self._parent,

            orient=tk.HORIZONTAL,
            command=self.xview
        )

        self.configure(
            xscrollcommand=self.sb_h_scrollbar.set,
            yscrollcommand=self.sb_v_scrollbar.set
        )

        self._canvas_frame = self.create_window(
            (0, 0),

            window=self.f_main_frame,
            anchor=self._canvas_anchor
        )

        self.f_main_frame.bind("<Configure>",
                               self._on_frame_configure)
        self.bind("<Configure>",
                  self._resize_frame)

    def _place_widgets(self):
        """ Places the scrollbars."""

        if self._horizontal_scroll:
            self.sb_h_scrollbar.pack(side='bottom',
                                     fill='x',
                                     expand=False)

        self.sb_v_scrollbar.pack(side='right',
                                 fill='y',
                                 expand=False)

    #########################################################################
    # Event handling

    def _on_frame_configure(
            self,

            _):
        self.configure(scrollregion=self.bbox("all"))

    def _resize_frame(
            self,

            event):

        # TODO

        # print('')
        # print('')

        # print(str(self.winfo_height()))
        available_height = event.height
        requested_height = self.f_main_frame.winfo_reqheight()

        # print(str(available_height))
        # print(str(requested_height))

        # print('')
        # print('')

        # print(str(self.winfo_width()))
        available_width = event.width
        requested_width = self.f_main_frame.winfo_reqwidth()

        # print(str(available_width))
        # print(str(requested_width))

        v = 1

        if v == 1:
            if self._horizontal_scroll:
                self.itemconfig(self._canvas_frame)
            else:
                self.itemconfig(self._canvas_frame,
                                width=event.width)
        else:
            if available_height >= requested_height:
                new_height = available_height
            else:
                new_height = requested_height

            if available_width >= requested_width:
                new_width = requested_width
            else:
                new_width = available_width

            self.itemconfig(self._canvas_frame, width=new_width, height=new_height)

    #########################################################################
