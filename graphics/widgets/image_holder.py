from PIL import Image, ImageTk

import constants.widget_constants as const
import tkinter as tk


class ImageHolder(tk.Frame):
    """ Frame that displays the image selected by the user and makes sure
    that that image has the maximum size in the available space while keeping
    the initial width/height ratio.
    """

    def __init__(self,

                 parent,

                 image_path_and_file_name: str):
        """
        :param parent: Parent.
        
        :param image_path_and_file_name: Path and name of the image.
        """

        tk.Frame.__init__(self, parent)

        self._display = tk.Canvas(
            self,
            highlightthickness=0
        )

        self._display.pack(side='top',
                           fill='y',
                           expand=True)

        self.bind("<Configure>", self._resize_event)

        self._open_image(image_path_and_file_name)

        self._draw_image(const.IHF_INITIAL_WIDTH,
                         const.IHF_INITIAL_HEIGHT)

    #########################################################################
    # Image handling

    def _open_image(
            self,

            image_path_and_file_name: str):
        """ Opens the image specified by image_path_and_file_name and
        determines the image ratio.

        :param image_path_and_file_name: Path and file name of the image.
        """

        self._image = Image.open(image_path_and_file_name)

        (self._im_width, self._im_height) = self._image.size

        self._w_ratio = self._im_height / self._im_width
        self._h_ratio = self._im_width / self._im_height

    def _draw_image(
            self,

            available_width: int,
            available_height: int):
        """
        :param available_width: Available width.
        :param available_height: Available height.
        """

        self._det_resize_dimensions(available_width,
                                    available_height)

        if self._new_width > 0 and self._new_height > 0:
            resized = self._image.resize(
                (
                    self._new_width,
                    self._new_height
                )
            )
            self.image = ImageTk.PhotoImage(resized)

            self._display.config(
                height=self._new_height,
                width=self._new_width,
                highlightthickness=0)

            self._display.create_image(
                0,
                0,
                image=self.image,
                anchor='nw',
                tags="IMG")

    def _det_resize_dimensions(
            self,

            available_width: int,
            available_height: int):
        """ Determines the dimensions to which to resize the image depending
        on holder's height and width.

        :param available_width: Available width.
        :param available_height: Available height.
        """

        if available_width <= available_height:
            self._smaller_width_math(available_width)

            if self._new_height > available_height:
                self._smaller_height_math(available_height)
        else:
            self._smaller_height_math(available_height)

            if self._new_width > available_width:
                self._smaller_width_math(available_width)

    def _resize_event(
            self,

            event):
        """ Automatically called when the parent's dimensions are changed,
        deletes the displayed image and redraws the original image, but with
        the new size.
        """

        self._display.delete("IMG")
        self._draw_image(event.width, event.height)

    def _smaller_width_math(
            self,

            available_width: int):
        """ New image's dimensions if the available width is smaller than
        the available height.

        :param available_width: Available width.
        """

        self._new_width = available_width
        self._new_height = int(available_width * self._w_ratio)

    def _smaller_height_math(
            self,

            available_height: int):
        """ New image's dimensions if the available height is smaller than
        the available width.

        :param available_height: Available height.
        """

        self._new_width = int(available_height * self._h_ratio)
        self._new_height = available_height

    #########################################################################
    # Public methods

    def update_image(
            self,

            image_path_and_file_name: str):
        """ Displays the image specify by the image_path_and_file_name
        parameter.

        :param image_path_and_file_name: Path and file name of the image.
        """

        self._open_image(image_path_and_file_name)
        self._draw_image(self._new_width,
                         self._new_height)

    #########################################################################
