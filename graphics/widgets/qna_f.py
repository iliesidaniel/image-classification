import constants.widget_constants as const
import tkinter as tk


class QnAF(tk.Frame):
    """
     - QnA = Question with n possible Answers;
     - Use this frame for a closed question with n possible answers.
    """

    def __init__(self,
                 parent,

                 frame_variable: tk.IntVar,

                 question_text: str,

                 answers_text: [],
                 answers_eh: [],

                 disabled=False):
        """
        :param parent: Parent.

        :param frame_variable: Frame variable.

        :param question_text: Question.
        :param answers_text: Lists with the answers.
        :param answers_eh: List with the event handlers.
        
        :param disabled:    - Default: False;
                            - If True all the widgets will be disabled.
        """

        tk.Frame.__init__(self,
                          parent,
                          padx=const.QNA_FRAME_PADX,
                          pady=const.QNA_FRAME_PADY)

        # Question text.
        self._lbl_question = tk.Label(
            self,
            text=question_text,
            font=const.QNA_FONT
        )

        # Answers frame
        self._f_answers = tk.Frame(
            self,

            padx=const.QNA_ANSWERS_FRAME_PADX,
            pady=const.QNA_ANSWERS_FRAME_PADY
        )

        # Answers
        self._rb_answers = []

        color = tk.Radiobutton()['background']

        for i in range(len(answers_text)):
            self._rb_answers.append(
                tk.Radiobutton(
                    self._f_answers,

                    padx=const.QNA_ANSWER_BUTTON_PADX,
                    pady=const.QNA_ANSWER_BUTTON_PADY,

                    font=const.QNA_FONT,
                    text=answers_text[i],

                    selectcolor=color,
                    relief='sunken',
                    bd=3,

                    variable=frame_variable,
                    command=answers_eh[i],
                    indicatoron=0,
                    value=i+1
                )
            )

        # Widget packing
        self._lbl_question.pack(side='top',
                                fill='both',
                                expand=True)

        for rb_answer in self._rb_answers:
            rb_answer.pack(side='left',
                           fill='both',
                           expand=True)

        self._f_answers.pack(side='top',
                             fill='both',
                             expand=True)

        if disabled:
            self.disable()

    #########################################################################
    # Public methods

    def update_question_text(
            self,

            new_question_text):
        """ 
        - Updates the question text.
        """

        self._lbl_question.config(text=new_question_text)

    # ~~~~~~~~~~~~~~~~~~~~~Select / deselect a specific button.~~~~~~~~~~~~~~

    def select_button(
            self,

            btn_index):
        """
        - Selects the buttons with the index equal to btn_index.
        - Index count starts from 0.

        :param btn_index: Index of te button to select.
        """

        self._rb_answers[btn_index].select()

    def deselect_button(
            self,

            btn_index):
        """
        - Deselects the buttons with the index equal to btn_index.
        - Index count starts from 0.

        :param btn_index: Index of te button to deselect.
        """

        self._rb_answers[btn_index].deselect()

    # ~~~~~~~~~~~~~~~~~~~~~Enable / disable a specific button.~~~~~~~~~~~~~~~

    def enable_button(
            self,

            btn_index):
        """
        - Enables the buttons with the index equal to btn_index.
        - Index count starts from 0.

        :param btn_index: Index of te button to enable.
        """

        self._rb_answers[btn_index].config(state='normal')

    def disable_button(
            self,

            btn_index):
        """
        - Disables the buttons with the index equal to btn_index.
        - Index count starts from 0.

        :param btn_index: Index of te button to disable.
        """

        self._rb_answers[btn_index].config(state='disabled')

    # ~~~~~~~~~~~~~~~~~~~~~Enable / disable the widget.~~~~~~~~~~~~~~~~~~~~~~

    def enable(self):
        """ Enables all the widgets."""

        self._lbl_question.config(state='normal')

        for rb_answer in self._rb_answers:
            rb_answer.config(state='normal')

    def disable(self):
        """ Disables all the widgets."""

        self._lbl_question.config(state='disabled')

        for rb_answer in self._rb_answers:
            rb_answer.config(state='disabled')

    #########################################################################
